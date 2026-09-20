import yt_dlp
from pathlib import Path

def yt_to_mp3(link: str) -> Path:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'paths': {
            'home': 'tmp/'
        },
        'outtmpl': {
            'default': '%(title)s.%(ext)s'
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        path = Path(ydl.prepare_filename(info)).with_suffix(".mp3")

    return path