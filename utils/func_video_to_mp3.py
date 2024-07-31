
from pytubefix import YouTube # Using pytubefix instead of pytube because of ongoing compatibility issues in this module
# Pytubefix Github: https://github.com/JuanBindez/pytubefix/tree/main
from pytubefix.cli import on_progress
import time
import sys
import os
 
def video_to_mp3(url, download_path):
    yt = YouTube(url, on_progress_callback=on_progress)
    
    # Clean the title for use in filenames
    safe_title = yt.title.replace(":", "_").replace("/", "_").replace("\\", "_").replace("?", "_").replace("!", "_")

    ys = yt.streams.get_audio_only()
    
    # Ensure the download path exists
    os.makedirs(download_path, exist_ok=True)
    
    # Download with a temporary name
    temp_file = ys.download(output_path=download_path)
    
    # Rename the file to the new safe title
    temp_file_name = os.path.basename(temp_file)
    new_file_name = safe_title + ".mp3"
    new_file_path = os.path.join(download_path, new_file_name)
    
    # Rename the file
    os.rename(temp_file, new_file_path)
    
    return new_file_path

if __name__ == "__main__":
    video_to_mp3(url="https://youtu.be/uryecU-Ttww", download_path=r"C:\Users\marc-\Documents\OneDrive\Documents\Loisirs\coding-projects\hebrew-transcription\mp3-files")
