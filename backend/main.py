from fastapi import FastAPI
from backend.schemas import ApplicationCreate

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/applications")
def create_application(application: ApplicationCreate):
    return application
