import yt_dlp


class MyLogger:
    def debug(self, msg):
        if "Downloading" in msg:
            print(msg)

    def warning(self, msg):
        print(f"Advertencia: {msg}")

    def error(self, msg):
        print(f"Error: {msg}")


def progress_hook(d):
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "").strip()
        if percent == "100.0%":
            return  # evitamos imprimir de nuevo cuando ya es 100%
        speed = d.get("_speed_str", "").strip()
        eta = d.get("_eta_str", "").strip()
        line = f"Descargando: {percent} | Velocidad: {speed} | Tiempo Estimado: {eta}"
        print(line.ljust(120), end="\r", flush=True)
    elif d["status"] == "finished":
        print("✅ ¡Descarga completada!".ljust(120))  # imprimimos línea nueva limpia


# Opciones de descarga, documentación en https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py
ydl_opts = {
    "quiet":True,
    "format": "(bestvideo[width>=1920]/bestvideo)+bestaudio/best",
    "download_archive": "ya_descargados.txt",
    "outtmpl": "E:/Servidor/Youtube/%(uploader)s/%(playlist_title)s/%(title)s.%(upload_date)s.%(ext)s",
    "restrictfilenames": True,
    "merge_output_format": "mkv",
    "ignoreerrors": True,
    "writesubtitles": True,
    "writeautomaticsub": True,
    "subtitleslangs": ["es", "en"],
    "writethumbnail": True,
    "writeinfojson": False,
    "logger": MyLogger(),
    "progress_hooks": [progress_hook],
    "ffmpeg_location": "./tools",
}

# Pedir la URL del video o lista
url = input("Pega con click derecho el video o la lista: ")

# Descargar el video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.list_subtitles
    ydl.download([url])
