import argparse
from pathlib import Path
from src.config import COMFY_URL, FPS, OUTPUT_DIR, TTS_VOICE, WORKFLOWS_DIR
from src.script_parser import load_script

def run_pipeline(script_file: str) -> None:
    script = load_script(script_file)
    title = script.get("title", "belgesel")
    scenes = script["scenes"]
    print(f"Proje baslatildi: {title} | Toplam sahne: {len(scenes)} | FPS: {FPS}")
    for idx, scene in enumerate(scenes, start=1):
        narration = scene.get("narration", "")
        visual_prompt = scene.get("visual_prompt", "")
        print(f"  [{idx}/{len(scenes)}] Ses: {narration[:45]}... | Gorsel: {visual_prompt[:45]}...")
    print(f"Cikti klasoru hazir: {OUTPUT_DIR} | ComfyUI: {COMFY_URL} | TTS: {TTS_VOICE} | Workflows: {WORKFLOWS_DIR}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AniDoc 2D belgesel otomasyon hattini calistirir.")
    parser.add_argument("--script", required=True, help="Senaryo JSON dosyasinin yolu")
    args = parser.parse_args()
    run_pipeline(args.script)
