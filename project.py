import sys
import re
from pytube import YouTube
from pytube import Playlist

def main():
    title()
    while(True):
        print("What do you want to download?")
        print("1 : Download 1 video")
        print("2 : Download multiple videos")
        print("3 : Download a playlist")
        print("4 : Exit")
        n=int(input())
        option(n)

def d_one_video(link):
    try:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download()
        print("Video Download Completed ✅")
    except :
        print("Technical Error...")

def d_playlist(link):
    try:
        playlist = Playlist(link)
        for vid in playlist.videos:
            d_one_video(vid.watch_url)
        print("Playlist Download Completed ✅")
    except Exception:
        print("Playlist does not exist")

def title():
    print(r"=====================================================================================================================")
    print()
    print(r" __     __         _         _             _    _ _____     _____                      _                 _           ")
    print(r" \ \   / /        | |       | |           | |  | |  __ \   |  __ \                    | |               | |          ")
    print(r"  \ \_/ /__  _   _| |_ _   _| |__   ___   | |__| | |  | |  | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ ")
    print(r"   \   / _ \| | | | __| | | | '_ \ / _ \  |  __  | |  | |  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|")
    print(r"    | | (_) | |_| | |_| |_| | |_) |  __/  | |  | | |__| |  | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   ")
    print(r"    |_|\___/ \__,_|\__|\__,_|_.__/ \___|  |_|  |_|_____/   |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   ")
    print()
    print("                                                                                                 BY JAKKU KARTHIK     ")
    print(r"=====================================================================================================================")

def option(n):
    match n:
        case 1:
            link = input("Enter the link : ")
            if re.search(r"(http(s)*:\/\/(www\.)*youtu(\.*)be)",link):
                d_one_video(link)
            else:
                print("Not a Youtube sharable video link")
        case 2:
            n=int(input("Number of videos to be downloaded : "))
            c=0
            for x in range(n):
                print("Enter link",x+1)
                s=input()
                if re.search(r"(http(s)*:\/\/(www\.)*youtu(\.*)be)",s):
                    d_one_video(s)
                    c=c+1
                else:
                    print("Not a Youtube sharable video link")
            if c>0:
                print(c,"Videos Download Completed ✅")
            else:
                print("Zero!!!, SERIOUSLY.....")
        case 3:
            link = input("Enter playlist link : ")
            if re.search(r"(http(s)*:\/\/(www\.)*youtu(\.*)be)",link):
                d_playlist(link)
            else:
                print("Please enter valid Playlist link")
        case 4:
             sys.exit()
        case _:
            print("Invalid input")

if __name__ == "__main__":
    main()
