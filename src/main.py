
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.database import Base, engine
from src.models.task import Task  # Register the Task model
from src.routers.task_router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Creates the tasks table only if it does not exist.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Week 1 Backend Engineering API",
    description="RESTful Task CRUD API using FastAPI and PostgreSQL",
    version="2.0.0",
    lifespan=lifespan,
)


app.include_router(task_router)


@app.get("/")
def home():
    return {"message": "Task CRUD API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
