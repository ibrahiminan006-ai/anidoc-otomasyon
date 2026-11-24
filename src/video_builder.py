import subprocess
from pathlib import Path

def build_final_video(clips: list[tuple[Path, Path]], output_path: str | Path, fps: int = 30) -> Path:
    """
    Sahne gorsel/kliplerini ve ses dosyalarini FFmpeg ile birlestirir.
    """
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    # FFmpeg kurulumunu dogrulamak icin ornek kontrol:
    subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    raise NotImplementedError("Sahne birlestirme ve altyazi FFmpeg adimi henuz yazilmadi.")
