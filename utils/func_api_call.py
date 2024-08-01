from openai import OpenAI
from func_video_to_mp3 import video_to_mp3
import tempfile


def create_api_client(api_key):
    client = OpenAI(api_key=api_key)
    return client

def transcription_api_call(audio_file, client):

    transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    language="he"
    )

    return transcript.text

def translation_api_call(transcript, client):
    '''
    A function to translate the transcription text using chat completion.
    Direct translation from the audio is possible using the Whisper model, but I use
    vanilla GPT model for money concerns.
    '''
    translation = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates Hebrew to English."},
            {"role": "user", "content": f'''I will give you a Hebrew text. First produce a transliteration and then an English translation. Delimitate transliteration and translation using the following format: "### Transliteration: \\nthe transliteration \\n### Translation: \\nthe translation" Here is the text: {transcript}'''}
        ]
    )

    return translation.choices[0].message.content


def main(url, api_key):
    with tempfile.TemporaryDirectory() as temp_dir:
    
        audio_file_path = video_to_mp3(url=url, temp_dir=temp_dir)
        
        with open(audio_file_path, "rb") as audio_file:
            client = create_api_client(api_key=api_key)
            transcript = transcription_api_call(audio_file=audio_file, client=client)
            translation = translation_api_call(transcript=transcript, client=client)

        return transcript, translation



if __name__ == "__main__":
    # transcript, translation = main(url="https://youtu.be/uryecU-Ttww", api_key=api_key)
    # print(transcript)
    # print(translation)

