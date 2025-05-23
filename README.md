# Descargador de Videos con yt-dlp

Este script en Python permite descargar videos o listas de reproducción desde YouTube y otros sitios compatibles usando [`yt-dlp`](https://github.com/yt-dlp/yt-dlp). Soporta resolución mínima 1080p, descarga de subtítulos en español e inglés, evita descargas duplicadas y organiza los videos automáticamente por canal y listas de reproducción.

---

## 🧰 Requisitos

- git
- [`uv`](https://github.com/astral-sh/uv) (como reemplazo de pip/pip-tools/virtualenv)
- [ffmpeg](https://ffmpeg.org/) instalado y accesible desde el sistema

---

## 📦 Instalación

1. **Instalar `uv` si aún no lo tenés:**

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

O en Windows (PowerShell):

```powershell
iwr https://astral.sh/uv/install.ps1 -useb | iex
```

2. **Clonar este repositorio y entrar a la carpeta:**

```bash
git clone https://github.com/tu-usuario/descargador-videos.git
cd descargador-videos
```

3. **Crear entorno virtual e instalar dependencias:**

```bash
uv init
uv sync
```

---

## 🛠 ffmpeg

Para combinar video y audio en un solo archivo `.mkv`, se usa `ffmpeg` disponible en la carpeta tools.

---

## 🚀 Uso

Ejecutá el script:

```bash
uv run main.py  
```

Pegá la URL del video o lista cuando la consola te lo solicite.

---

## 📂 Estructura del guardado

Los videos se almacenan en:

```
E:/Servidor/Videos/{uploader}/{playlist_title}/{upload_date}.{title}.{id}.{ext}
```

---

## 🧠 Características

- ✅ Soporte para videos individuales y listas de reproducción
- ✅ Evita descargar videos ya procesados (archivo `ya_descargados.txt`)
- ✅ Guarda archivos organizados por canal y lista
- ✅ Muestra progreso de las descargas
- ✅ Descarga subtítulos en español e inglés (si están disponibles), trata de bajar los generados automáticamente
- ✅ Combina video y audio en `.mkv` (requiere `ffmpeg`)
- ✅ Manejo robusto de errores con la clase YoutubeDL

---

## 📝 Notas

- Si `playlist_title` no existe (por ejemplo, no es una lista), el video se guarda directamente bajo la carpeta del uploader.
- Si `ffmpeg` no está instalado correctamente, verás una advertencia y los archivos no se combinarán.

---

## 📝 Licencia

Este script es de uso libre y puede adaptarse según tus necesidades.
