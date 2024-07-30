from openai import OpenAI
from utils.func_video_to_mp3 import video_to_mp3
from dotenv import find_dotenv, load_dotenv
import os


def create_api_client():
    client = OpenAI()
    return client

def transcription_api_call(audio_file, client):

    transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    language="he"
    )

    return transcript.text

def translation_api_call(transcript):
    '''
    A function to translate the transcription text using chat completion.
    Direct translation from the audio is possible using the Whisper model, but I use
    vanilla GPT model for money concerns.
    '''
    translation = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates Hebrew to English."},
            {"role": "user", "content": f'I will give you a Hebrew text. First produce a transliteration and then an English translation. Here is the text: {transcript}'}
        ]
    )

    print(translation.choices[0].message.content)

def main(url):
    load_dotenv(dotenv_path=r"C:\Users\marc-\Documents\OneDrive\Documents\Loisirs\coding-projects\hebrew-transcription\utils\myenv.env")
    download_path=r"C:\Users\marc-\Documents\OneDrive\Documents\Loisirs\coding-projects\hebrew-transcription\mp3-files"
    
    audio_file = video_to_mp3(url=url, download_path=download_path)
    audio_file_path = 
    client = create_api_client()
    transcript = transcription_api_call(audio_file=audio_file, client=client)
    print(transcript)
    translation_api_call(transcript=transcript)



if __name__ == "__main__":
    load_dotenv(dotenv_path=r"C:\Users\marc-\Documents\OneDrive\Documents\Loisirs\coding-projects\hebrew-transcription\utils\myenv.env")

    audio_file = open(r"C:\Users\marc-\Documents\OneDrive\Documents\Loisirs\coding-projects\hebrew-transcription\mp3-files\hebrew-vid-1.mp3", "rb")
    client = create_api_client()
    transcript = transcription_api_call(audio_file)
    print(transcript)
    translation_api_call(transcript=transcript)

