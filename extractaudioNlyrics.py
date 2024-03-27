from pytube import YouTube
from moviepy.editor import *  
import datetime
import os
import requests
import re
current = "Enter file location" # swap \ with /

hyperlinks = []
yt = YouTube('https://youtu.be/XXHC4emaVVI')
yt.streams.filter(only_audio=True).first().download()
duration = yt.length
name = yt.title
sepindex = name.find(" - ")
song_title = name[:sepindex].strip()

added_folder_name = current + "/" + str(song_title)
os.makedirs(added_folder_name)
video_path = yt.streams.filter(only_audio=True).first().default_filename
audio = AudioFileClip(video_path)
audio.write_audiofile(added_folder_name + "/" + str(song_title) + ".wav")
lyrics_directory = os.makedirs(added_folder_name + "/" + str(song_title) + "lyrics")

full_html = requests.get("https://youtu.be/XXHC4emaVVI").text
y = re.search(r'shortDescription":"', full_html)
desc = ""
count = y.start() + 19  # adding the length of the 'shortDescription":"
while True:
    # get the letter at current index in text
    letter = full_html[count]
    if letter == "\"":
        if full_html[count - 1] == "\\":
            # this is case where the letter before is a backslash, meaning it is not real end of description
            desc += letter
            count += 1
        else:
            break
    else:
        desc += letter
        count += 1

lsep = desc.find("]")
lyrics = desc[lsep+1:]
lyrics = re.sub("\[\w*\s*\w*\]","",lyrics)
list1 = lyrics.split('\\n')
lyriclist = [x for x in list1 if x!=""]
print(lyriclist)
for i in range(len(lyriclist)):
    filename = added_folder_name + "/" + str(song_title) + "lyrics" + "/" + str(i) + ".txt"
    with open(filename, "w",encoding='utf-8') as file:
        # Use the writelines() method to write each line of the list to the file
        file.write(lyriclist[i])
os.remove(name + ".mp4")







