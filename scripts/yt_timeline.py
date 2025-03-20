import json
from argparse import ArgumentParser
import subprocess
import os
from datetime import datetime, UTC

import yt_dlp

def arguments():
  a = ArgumentParser()
  a.add_argument("--file", required=True)
  a.add_argument(
    "--stages", nargs="+", default=[0,1], choices=[0,1], type=int,
    help="Stages to run"
  )
  a.add_argument("--cache-file", default="cache.json")
  a.add_argument("--markwhen", default="tmp.mw", help="Store a markwhen file somewhere")
  return a.parse_args()


def main():
  args = arguments()

  if 0 in args.stages: stage_0(args)
  if 1 in args.stages: stage_1(args)

def stage_0(args):
  with open(args.file, "r") as f:
    data = json.load(f)

  ydl = yt_dlp.YoutubeDL() if yt_dlp is not None else None

  entries = []
  if os.path.exists(args.cache_file):
    with open(args.cache_file, "r") as c:
      entries = json.load(c)

  i = 0
  for d in data["messages"]:
    if d["isUnsent"]: continue

    text = d["text"]
    if "http" not in text: continue

    is_yt = "youtu" in text
    entry = { "url": text, "timestamp": d["timestamp"] }

    if i < len(entries) and entries[i]["url"] == text:
      i += 1
      continue
    i += 1

    if not is_yt:
      entries.append(entry)
      continue

    try:
      info = ydl.extract_info(text, download=False)
    except:
      i -= 1;
      continue

    entry["title"] = info["title"]
    entry["tags"] = info["tags"]

    entries.append(entry)

    if i % 5 == 0:
      with open(args.cache_file, "w") as c:
        json.dump(entries, c, indent=2)


  with open(args.cache_file, "w") as c:
    json.dump(entries, c, indent=2)


  return
def stage_1(args):
  with open(args.cache_file, "r") as c:
    entries = json.load(c)
  if args.markwhen is not None:
    markwhen(entries, args)

def markwhen(entries, args):
  print(f"Making timeline for {len(entries)} entries")
  f = open(args.markwhen, "w")
  for e in entries:
    time = datetime\
      .fromtimestamp(int(e["timestamp"]) / 1000, UTC)\
      .strftime('%Y-%m-%d %H:%M')
    url = e['url']
    if 'title' in e:
      title = e['title']
      title = title.replace("[", "「")
      title = title.replace("]", "」")
      f.write(f"{time}: [{title}]({url})\n")
    else:
      f.write(f"{time}: [{url}]({url})\n")
  f.close()

  assert(not os.system(f"mw {args.markwhen} yt_timeline.html"))

  with open("yt_timeline.html", "r") as f:
    data = f.read()
  data = data.replace("Markwhen Timeline", "Music Timeline")

  with open("yt_timeline.html", "w") as f:
    f.write(data)


if __name__ == "__main__": main()

