
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Week 1 Backend Engineering",
    description="Task REST API for Tuesday training",
    version="1.1.0",
)


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def home():
    return {"message": "Week 1 Backend API is running"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Week 1 Backend API",
    }


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return task


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    global next_task_id

    task = Task(
        id=next_task_id,
        title=task_data.title,
        description=task_data.description,
        completed=False,
    )
    tasks[next_task_id] = task
    next_task_id += 1

    return task
