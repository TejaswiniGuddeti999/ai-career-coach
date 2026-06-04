
from fastapi import FastAPI, UploadFile, File, Form
from routes.analyze import router

app = FastAPI(title="AI Career Coach")
app.include_router(router)

@app.get("/")
def home():
    return {'message':'AI Career Coach is running'}