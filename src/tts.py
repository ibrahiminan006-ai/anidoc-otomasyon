from pathlib import Path

def synthesize_narration(text: str, out_path: str | Path, voice: str = "tr-TR-EmelNeural") -> Path:
    """
    Sahne metnini ses dosyasina cevirir.
    Bir sonraki adimda buraya ucretsiz Turkce TTS (orn. edge-tts veya yerel model) baglanacak.
    """
    target = Path(out_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError(
        f"TTS motoru henuz baglanmadi. Metin: '{text[:40]}...' -> Hedef: {target} (Ses: {voice})"
    )
