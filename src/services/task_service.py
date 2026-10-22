
from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.repositories import task_repository
from src.schemas.task_schema import TaskCreate, TaskUpdate


def create_task(db: Session, data: TaskCreate, user_id: int):
    values = data.model_dump()

    is_completed = values["status"] == "COMPLETED"
    values["completed"] = is_completed
    values["completed_at"] = datetime.now(timezone.utc) if is_completed else None

    return task_repository.create_task(db, values, user_id)


def list_tasks(db: Session, user_id: int):
    return task_repository.list_tasks(db, user_id)


def get_task(db: Session, task_id: int, user_id: int):
    task = task_repository.get_task(db, task_id, user_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


def update_task(
    db: Session,
    task_id: int,
    data: TaskUpdate,
    user_id: int,
):
    task = get_task(db, task_id, user_id)
    changes = data.model_dump(exclude_unset=True)

    for field in ("title", "status", "priority"):
        if field in changes and changes[field] is None:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"{field} cannot be null",
            )

    if "status" in changes:
        is_completed = changes["status"] == "COMPLETED"
        changes["completed"] = is_completed

        if is_completed:
            if task.status != "COMPLETED":
                changes["completed_at"] = datetime.now(timezone.utc)
        else:
            changes["completed_at"] = None

    return task_repository.update_task(db, task, changes)


def delete_task(db: Session, task_id: int, user_id: int):
    task = get_task(db, task_id, user_id)
    task_repository.delete_task(db, task)
