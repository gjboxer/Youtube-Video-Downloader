from pytube import YouTube
from pytube import Playlist
choice=int(input("Enter 1 for playlist or 2 for video: "))
print("Enter link of youtube video: ")
link = input()
if choice==2:
    yt1=YouTube(link)
    videos = yt1.streams.get_highest_resolution()
    videos.download()
elif choice ==1:
    py=Playlist(link)
    print(f'Downloading : {py.title}')
    for video in py.videos:
        video.streams.first().download
print("Downloaded")