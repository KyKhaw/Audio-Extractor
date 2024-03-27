from pytube import YouTube
from moviepy.editor import *  
import datetime
import os
import requests
import re
current = "C:/Users/Yuan/Desktop/NovBeeVSCode/MiscSongs"

hyperlinks = []
yt = YouTube('https://youtu.be/hI4HND3ZG58')
yt.streams.filter(only_audio=True).first().download()
name = yt.title[1:10]

video_path = yt.streams.filter(only_audio=True).first().default_filename
audio = AudioFileClip(video_path)
audio.write_audiofile(current + "/" + str(name) + ".wav")
os.remove(name + ".mp4")
