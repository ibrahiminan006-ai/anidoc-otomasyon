import json
from pathlib import Path

def load_script(script_path):
    data = json.loads(Path(script_path).read_text(encoding="utf-8-sig"))
    if not isinstance(data.get("scenes"), list):
        raise ValueError("Senaryo dosyasi scenes listesi icermelidir.")
    return data
