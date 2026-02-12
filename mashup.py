import os
import yt_dlp
from pydub import AudioSegment
from moviepy.video.io.VideoFileClip import VideoFileClip

def run_mashup(singer, num_videos, duration, output_file):
    try:
        # Create folders
        os.makedirs("videos", exist_ok=True)
        os.makedirs("audios", exist_ok=True)
        os.makedirs("trimmed", exist_ok=True)

        # Download videos
        search_query = f"ytsearch{num_videos}:{singer} official song"
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'videos/%(title)s.%(ext)s',
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_query])

        # Convert to audio
        for file in os.listdir("videos"):
            if file.endswith(".mp4"):
                video_path = os.path.join("videos", file)
                audio_path = os.path.join("audios", file.replace(".mp4", ".mp3"))

                clip = VideoFileClip(video_path)
                clip.audio.write_audiofile(audio_path)
                clip.close()

        # Trim
        for file in os.listdir("audios"):
            if file.endswith(".mp3"):
                audio_path = os.path.join("audios", file)
                trimmed_path = os.path.join("trimmed", file)

                audio = AudioSegment.from_mp3(audio_path)
                trimmed = audio[:duration * 1000]
                trimmed.export(trimmed_path, format="mp3")

        # Merge
        final_audio = AudioSegment.empty()

        for file in os.listdir("trimmed"):
            if file.endswith(".mp3"):
                audio_path = os.path.join("trimmed", file)
                sound = AudioSegment.from_mp3(audio_path)
                final_audio += sound

        final_audio.export(output_file, format="mp3")

        print("Mashup created successfully!")

    except Exception as e:
        print("Error:", e)
