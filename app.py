import streamlit as st
from utils.func_api_call import main
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
import os

st.title("Video transcriber and translator")
st.write("Enter the URL of a YouTube video to get the text transcription, transliteration and translation.")

url = st.text_input("YouTube video URL")

if st.button("Translate"):
    if url:
        main(url=url)
    else:
        st.error("Please enter a valid YouTube URL.")

if __name__ == "__main__":
    main(url="https://youtu.be/uryecU-Ttww")