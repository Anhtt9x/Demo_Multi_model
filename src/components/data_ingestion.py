from src.utils.utils import download_youtube_video, video_to_image
import os

output_video_path = os.path.join(os.getcwd(), 'video_path')
output_folder = os.path.join(os.getcwd(), 'mixed_data')
output_audio_path = os.path.join(output_folder, 'output_audio.wav')

os.makedirs(output_folder,exist_ok=True)

file_path = os.path.join(output_video_path,"input_vid.mp4")

video_url = 'https://www.youtube.com/watch?v=B5kFQCbJUq0&list=RDer01Kzr5lTk&index=2'
metadata = download_youtube_video(video_url, output_video_path)
print(metadata)

video_to_image(file_path, output_folder)

