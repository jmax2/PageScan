from __future__ import annotations

from pathlib import Path

from PIL import Image


def ensure_parent_dir(path: str | Path) -> Path:
    """Create the parent directory for a target file if it doesn't exist."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    return file_path


def load_image(image_path: str | Path) -> Image.Image:
    """Load an image from disk and return a Pillow image object."""
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    with Image.open(path) as img:
        # Copy image data so callers can safely process and save without mutating the source.
        image_copy = img.copy()

    return image_copy
