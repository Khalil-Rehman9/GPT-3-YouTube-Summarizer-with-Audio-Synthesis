import openai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS 
import io
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Video Summarizer", page_icon=":movie_camera:")

st.title("YouTube Video Summarizer")

@st.cache_resource
def get_transcript(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split("v=")[-1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = ' '.join([line['text'] for line in transcript]) 
    return text

@st.cache_resource
def summarize(transcript):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt = f"Generate a concise summary of the following content in approximately 400 words: \n\n{transcript}",
        max_tokens=400,
        n=1,
        stop=None,
        temperature=0.5,
    )
    summary = response.choices[0].text.strip()
    return summary

@st.cache_resource
def text_to_speech(text):
    tts = gTTS(text, lang='en', slow=False)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp.read()

video_url = st.text_input("Enter YouTube Video URL:")
if video_url:
    
    transcript = get_transcript(video_url)
    
    st.subheader("Full Transcript")
    st.write(transcript)
    
    summarizer = summarize(transcript)
    
    st.subheader("Summary")
    st.write(summarizer)
    
    audio = text_to_speech(summarizer)
    st.audio(io.BytesIO(audio), format='audio/mp3')

else:
    st.write("Enter a YouTube URL above to get started!")
