import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'ffmpeg_location': r'C:\ffmpeg\bin',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtube.com/watch?v=i_kF4zLNKio&list=RDi_kF4zLNKio&start_radio=1'])

# ffmpeg
# open powershell
# justpaste.it/iq3it
# winget install --id Gyan.FFmpeg -e
#     'ffmpeg_location': r'C:\ffmpeg\bin',
