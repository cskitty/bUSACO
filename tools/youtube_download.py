import sys
from pytube import YouTube

#ask for the link from user
# link = input("Enter the link of YouTube video you want to download:  ")
link = sys.argv[1]
print(link)
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")