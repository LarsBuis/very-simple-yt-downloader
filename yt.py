from pytube import YouTube
import os
from time import sleep
from os import system, name

while True:
    print("""
     __   _____  _   _ _____ _   _ ____  _____   ____  _     
     \ \ / / _ \| | | |_   _| | | | __ )| ____| |  _ \| |    
      \ V / | | | | | | | | | | | |  _ \|  _|   | | | | |    
       | || |_| | |_| | | | | |_| | |_) | |___  | |_| | |___ 
       |_| \___/ \___/  |_|  \___/|____/|_____| |____/|_____| made by Yuniqe
                                                                                    
    """)

    def clear():
        if name == 'nt':
            _ = system('cls')
  
        else:
            _ = system('clear')

    def audio():
        video = yt.streams.filter(only_audio=True).first()

        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'

        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(yt.title + " has been successfully downloaded.")
        sleep(3)
        clear()
        return

    def video():
        ys = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'
        out_file = ys.download(output_path=destination)
        
        print(yt.title + " has been successfully downloaded.")
        sleep(3)
        clear()        
        return 

    link = input("Enter the link of YouTube video you want to download:  ")
    yt = YouTube(link)
    print("Title: ",yt.title)
    a_or_v = input("do you want video or audio?: ")

    if a_or_v == 'audio':
        audio()
    elif a_or_v == 'video':
        video()
    elif a_or_v != 'audio' or 'video':
        print('try again')
