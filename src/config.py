import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
WORKFLOWS_DIR = BASE_DIR / "workflows"
ASSETS_DIR = BASE_DIR / "assets"
OUTPUT_DIR = BASE_DIR / "output"
SCRIPTS_DIR = BASE_DIR / "scripts"

COMFY_URL = os.getenv("COMFY_URL", "http://127.0.0.1:8188")
TTS_VOICE = os.getenv("TTS_VOICE", "tr-TR-EmelNeural")
FPS = int(os.getenv("VIDEO_FPS", "30"))
WIDTH = int(os.getenv("VIDEO_WIDTH", "1920"))
HEIGHT = int(os.getenv("VIDEO_HEIGHT", "1080"))

for d in (WORKFLOWS_DIR, ASSETS_DIR, OUTPUT_DIR, SCRIPTS_DIR):
    d.mkdir(parents=True, exist_ok=True)
