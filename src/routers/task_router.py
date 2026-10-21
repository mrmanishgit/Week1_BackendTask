
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from src.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

DbSession = Annotated[Session, Depends(get_db)]


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(data: TaskCreate, db: DbSession):
    return task_service.create_task(db, data)


@router.get("", response_model=list[TaskResponse])
def get_all_tasks(db: DbSession):
    return task_service.get_all_tasks(db)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: DbSession):
    return task_service.get_task(db, task_id)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, db: DbSession):
    return task_service.update_task(db, task_id, data)


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(task_id: int, db: DbSession):
    task_service.delete_task(db, task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
