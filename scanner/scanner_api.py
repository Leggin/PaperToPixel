import io
import os
from contextlib import asynccontextmanager
import uuid
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import rembg
from PIL import Image
import config

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
# )


@asynccontextmanager
async def lifespan(application: FastAPI) -> None:
    if not os.path.exists(config.SAVE_IMAGE_DIR):
        os.makedirs(config.SAVE_IMAGE_DIR)
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)) -> JSONResponse:
    # Read the uploaded image
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    # Use rembg to remove the background
    output = rembg.remove(image)

    processed_image_path = f"{config.SAVE_IMAGE_DIR}/{uuid.uuid4()}.png"
    output.thumbnail(config.IMAGE_SIZE, Image.Resampling.LANCZOS)
    output.save(processed_image_path, "PNG")

    return JSONResponse(content={"message": "Background removed successfully"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
