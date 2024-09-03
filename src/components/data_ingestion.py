from src.utils.utils import download_youtube_video, video_to_image,video_to_audio,audio_to_text
import os

output_video_path = os.path.join(os.getcwd(), 'video_path')
output_folder = os.path.join(os.getcwd(), 'mixed_data')
output_audio_path = os.path.join(output_folder, 'output_audio.wav')

os.makedirs(output_folder,exist_ok=True)

file_path = os.path.join(output_video_path,"input_vid.mp4")

video_url = 'https://youtu.be/3dhcmeOTZ_Q'
metadata = download_youtube_video(video_url, output_video_path)
print(metadata)

video_to_image(file_path, output_folder)

video_to_audio(file_path,output_audio_path)

text_data = audio_to_text(output_audio_path)

with open(os.path.join(output_folder,"output_text.txt"), "w") as file:
    file.write(text_data)
    print("Audio to Text Conversion Successful!")

