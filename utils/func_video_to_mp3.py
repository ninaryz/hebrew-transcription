
from pytubefix import YouTube # Using pytubefix instead of pytube because of ongoing compatibility issues in this module
# Pytubefix Github: https://github.com/JuanBindez/pytubefix/tree/main
from pytubefix.cli import on_progress
import os
 
def video_to_mp3(url, temp_dir):
    yt = YouTube(url, on_progress_callback=on_progress)
    
    # Clean the title for use in filenames
    safe_title = yt.title.replace(":", "_").replace("/", "_").replace("\\", "_").replace("?", "_").replace("!", "_")

    ys = yt.streams.get_audio_only()

    temp_file_path = ys.download(output_path=temp_dir)

    # Generate a new file path with the safe title
    new_file_name = safe_title + ".mp3"
    new_file_path = os.path.join(temp_dir, new_file_name)
    
    # Rename the file
    os.rename(temp_file_path, new_file_path)
    
    # Return the path of the new file
    return new_file_path

