#Youtube Song Extractor
1. Under the extractaudio.py file, locate part of the code: yt = Youtube("Paste youtube link here")
2. Specify the file location by altering the 'current' variable
3. Run the code
4. The code produces the song in wav format stored in the specified location

#Youtube Song & Lyrics Extractor
1. Under the extractaudioNlyrics.py file, locate part of the code: yt = Youtube("Paste youtube link here") &
   full_html = requests.get("Paste youtube link here").text
2. Specify the file location by altering the 'current' variable
3. Run the code
4. The code produces a folder in the specified location, storing the song in wav format, along with a folder storing the line-by-line lyrics
