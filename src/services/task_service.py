
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models.task import Task
from src.repositories import task_repository
from src.schemas.task_schema import TaskCreate, TaskUpdate


def create_task(db: Session, data: TaskCreate) -> Task:
    return task_repository.create_task(db, data)


def get_all_tasks(db: Session) -> list[Task]:
    return task_repository.get_all_tasks(db)


def get_task(db: Session, task_id: int) -> Task:
    task = task_repository.get_task_by_id(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


def update_task(
    db: Session,
    task_id: int,
    data: TaskUpdate,
) -> Task:
    task = get_task(db, task_id)
    return task_repository.update_task(db, task, data)


def delete_task(db: Session, task_id: int) -> None:
    task = get_task(db, task_id)
    task_repository.delete_task(db, task)
