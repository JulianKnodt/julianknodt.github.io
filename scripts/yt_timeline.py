import json
from argparse import ArgumentParser
import subprocess
import os

import yt_dlp

def arguments():
  a = ArgumentParser()
  a.add_argument("--file", required=True)
  a.add_argument(
    "--stages", nargs="+", default=[0,1], choices=[0,1], type=int,
    help="Stages to run"
  )
  a.add_argument("--cache-file", default="cache.json")
  return a.parse_args()


def main():
  args = arguments()

  if 0 in args.stages: stage_0(args)
  if 1 in args.stages: stage_1(args)

def stage_0(args):
  with open(args.file, "r") as f:
    data = json.load(f)

  ydl = yt_dlp.YoutubeDL()

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
    print(text)

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


if __name__ == "__main__": main()

