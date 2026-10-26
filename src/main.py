
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.database import Base, engine 
from src.models import task, user
from src.routers.auth_router import router as auth_router
from src.routers.task_router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Creates missing tables; does not migrate existing tables.
    Base.metadata.create_all(bind=engine)
    yield




app = FastAPI(
    title="Task Management System API",
    description="JWT-secured task management with PostgreSQL",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(task_router)


@app.get("/")
def root():
    return {"message": "Task Management System API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
