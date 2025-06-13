# import subprocess

# command = '''ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf 
# "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v 
# libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p reel.mp4 '''


# try :
#     subprocess.run(command,shell=True,check=True)
#     print("Ffmpeg executed succefully!")

# except subprocess.CalledProcessError as e:
#     print(f"Error printinf ffmpeg command: {e}")



import subprocess


def ffm():

    # Define the complex video filter string separately
    video_filter = "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:1920:(oh-ih)/2:0:black"
    video1 = "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black"
    # Construct the command as a list of arguments
    command_args = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'user_uploads/{folder}/input.txt',
        '-i', 'user_uploads/{folder}/audio.mp3',
        
        '-vf', video1,  # The entire filter string as one element
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-shortest',
        '-r', '30',
        '-pix_fmt', 'yuv420p',
        'static/reels/{folder}.mp4'
    ]

    try:
        # Do NOT use shell=True when passing a list of arguments
        subprocess.run(command_args, check=True)
        print("FFmpeg command executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error executing FFmpeg command: {e}")
    except FileNotFoundError:
        print("Error: FFmpeg executable not found. Make sure it's in your PATH.")


ffm()