# config.py
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
)
ASSET_PATH = os.path.join(BASE_DIR, "assets")
TEXTURE_PATH = os.path.join(ASSET_PATH, "textures")
