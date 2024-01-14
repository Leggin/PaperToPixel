import os

SAVE_IMAGE_DIR = os.getenv("SAVE_IMAGE_DIR", "images")
IMAGE_SIZE = (500, 500)
API_BASE_URL = os.getenv("API_BASE_URL", "http://0.0.0.0:8000")
