from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
from prediction import prediction
from scraping import scraping
app = FastAPI()

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    name = prediction(image)
    details = scraping(name)
    return details
