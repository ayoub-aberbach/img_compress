import os
import secrets
from PIL import Image
from pathlib import Path


def compress_image(image_name: Path, upload_folder: Path, compressed_folder: Path):
    filepath: Path = os.path.join(upload_folder, image_name)
    picture = Image.open(filepath)

    saved_image = f"{secrets.token_hex(8)}.{picture.format}"
    compressed_image: Path = os.path.join(compressed_folder, saved_image)

    if picture.format == "JPEG":
        picture.save(compressed_image, "JPEG", optimize=True)

    if picture.format == "PNG":
        picture.save(compressed_image, "PNG", optimize=True)

    if picture.format == "JPG":
        picture.save(compressed_image, "JPG", optimize=True)

    return compressed_image
