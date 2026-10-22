
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.models.user import User
from src.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from src.security.jwt import get_current_user
from src.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return task_service.create_task(db, data, current_user.id)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return task_service.list_tasks(db, current_user.id)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return task_service.get_task(db, task_id, current_user.id)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return task_service.update_task(db, task_id, data, current_user.id)



@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task_service.delete_task(db, task_id, current_user.id)

    return {
        "message": "Task deleted successfully",
        "task_id": task_id,
    }

