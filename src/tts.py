import asyncio
from pathlib import Path
import edge_tts

async def _save_tts(text: str, target: Path, voice: str) -> None:
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(target))

def synthesize_narration(text: str, out_path: str | Path, voice: str = "tr-TR-EmelNeural") -> Path:
    target = Path(out_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    asyncio.run(_save_tts(text, target, voice))
    return target
