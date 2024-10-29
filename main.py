import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from PIL import Image
import uuid

# 업로드 폴더 설정
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")

@app.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # 파일 처리 및 저장 로직
    file_location = os.path.join(UPLOAD_FOLDER, f"uploaded_{uuid.uuid4().hex}.jpg")
    with open(file_location, "wb") as file_object:
        file_object.write(await file.read())
    return {"info": f"file saved at {file_location}"}

# 이미지 리사이징 및 다운로드 관련 코드 추가
