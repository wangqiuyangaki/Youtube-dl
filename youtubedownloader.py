
from __future__ import unicode_literals
import youtube_dl

def download():
    x=input("input your download link:")
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([x])

download()