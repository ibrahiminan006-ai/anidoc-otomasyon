from pathlib import Path

def generate_scene_visual(prompt: str, workflow_path: str | Path, out_path: str | Path, comfy_url: str) -> Path:
    """
    ComfyUI API uzerinden sahne gorseli veya klibi uretir.
    Bulut GPU baglandiginda bu fonksiyon ComfyUI /prompt ucuna istek atacak.
    """
    target = Path(out_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    raise NotImplementedError(
        f"ComfyUI istemcisi henuz baglanmadi ({comfy_url}). Workflow: {workflow_path}"
    )
