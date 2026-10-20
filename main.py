
from fastapi import FastAPI

app = FastAPI(
    title="Week 1 Backend Engineering",
    description="Backend engineering practice using FastAPI",
    version="1.0.0",
)

@app.get("/")
def home():
    return {"message": "Week 1 Backend API is running"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Week 1 Backend API",
    }
