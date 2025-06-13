#this file looks for a new folders inside user upload and converts them to reel if they are not already converted 

import os
from text_To_audio import text_to_speech_file
import time
import subprocess


def text_to_audio(folder):
    print("TTA - ",folder)
    desc_path = f"user_uploads/{folder}/desc.txt"
    if not os.path.exists(desc_path):
        print(f"desc.txt not found in {folder}")
        return
    with open(desc_path) as f:
        text = f.read()

     
        
    print(text,folder)
    text_to_speech_file(text,folder)
def create_reels(folder):
    video1 = "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black"
    command_args = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', f'user_uploads/{folder}/input.txt',
        '-i', f'user_uploads/{folder}/audio.mp3',
        
        '-vf', video1,  # The entire filter string as one element
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-shortest',
        '-r', '30',
        '-pix_fmt', 'yuv420p',
        f'static/reels/{folder}.mp4'
    ]
    subprocess.run(command_args,check=True)
    print("CR - " , folder)

if __name__ == "__main__":
    while True:
        print("Processing queue....")
        with open("done.txt", "r") as f:
            done_folders = f.readlines()

        
        done_folders = [f.strip() for f in done_folders]
        folders = os.listdir("user_uploads")
        
        for folder in folders:
            if(folder not in done_folders):
                text_to_audio(folder) # genrate the audio.mpe from the desc.text
                create_reels(folder) # converts the image and audio.mp3 inside the folder to a reel
                with open ("done.txt","a") as f:
                    f.write(folder + "\n")
        time.sleep(4)