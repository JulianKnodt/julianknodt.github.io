## Remove Dead Youtube Links

I wrote this python script that will parse all the youtube videos in playlist.md, check if the video is still available, and remove any videos that are no longer available from the page. You can check which are the dead links afterwards in dead_links.txt

You will need python and youtube-dl [https://github.com/ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl). It also uses tqdm for the status bar. You should be able to get it from pip or just remove the tqdm.tqdm wrapper around the iterable. 

I did this in like an hour procrastinating. Worked on Windows 10 running python version 3.9.5 and youtube-dl 2021.05.16

Easiest way to use it:

```
cp ../playlist.md .
python3 remove_dead_yt_links.py
mv new_playlist.md ../playlist.md
rm dead_links.txt
```
