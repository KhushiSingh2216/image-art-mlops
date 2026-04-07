from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from PIL import Image
import numpy as np
import io
import logging
from app.model import pencil_sketch, ink_sketch, cartoon_effect

app = FastAPI()

# logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# read uploaded image
def read_image(file):
    contents = file.file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    return np.array(img)

# save output
def save_image(arr, path):
    Image.fromarray(arr).save(path)

@app.get("/")
def home():
    return {"message": "API Running 🚀"}

# sketch endpoint
@app.post("/sketch")
async def sketch_api(file: UploadFile = File(...)):
    img = read_image(file)
    sketch = pencil_sketch(img)

    path = "outputs/sketch.png"
    save_image(sketch, path)

    logging.info("Sketch created")
    return FileResponse(path)

# ink endpoint
@app.post("/ink")
async def ink_api(file: UploadFile = File(...)):
    img = read_image(file)
    sketch = pencil_sketch(img)
    ink = ink_sketch(sketch)

    path = "outputs/ink.png"
    save_image(ink, path)

    logging.info("Ink created")
    return FileResponse(path)

# cartoon endpoint
@app.post("/cartoon")
async def cartoon_api(file: UploadFile = File(...)):
    img = read_image(file)
    cartoon = cartoon_effect(img)

    path = "outputs/cartoon.png"
    save_image(cartoon, path)

    logging.info("Cartoon created")
    return FileResponse(path)