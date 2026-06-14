import os

class Config:
    SECRET_KEY = "careerhelper"
    UPLOAD_FOLDER = "uploads"

if not os.path.exists("uploads"):
    os.makedirs("uploads")