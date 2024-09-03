from moviepy.editor import VideoFileClip
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path
import speech_recognition as sr
from matplotlib import pyplot as plt
from PIL import Image
from pprint import pprint
import os


def video_to_image(video_path, output_path):
  video_clip = VideoFileClip(video_path)
  video_clip.write_images_sequence(os.path.join(output_path,"frame_%04d.jpg"),fps=0.2)


def video_to_audio(video_path, output_path):
  video_clip = VideoFileClip(video_path)
  audio_clip = video_clip.audio
  audio_clip.write_audiofile(output_path)


def audio_to_text(audio_path):
  recognizer = sr.Recognizer()
  with sr.AudioFile(audio_path) as source:
    audio_data = recognizer.record(source)
    try:
      text = recognizer.recognize_whisper(audio_data)
    except sr.UnknownValueError:
      text = "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
      text = f"Could not request results from Google Speech Recognition service; {e}"
  return text


def download_youtube_video(video_url, output_path):
  yt = YouTube(video_url, on_progress_callback = on_progress)
  meta = {"Author":yt.author,"Titile":yt.title,"Views":yt.views}
  video_stream = yt.streams.get_highest_resolution()
  video_stream.download(output_path=output_path, filename='input_vid.mp4')

  return meta

