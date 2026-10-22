
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.task import Task


def create_task(db: Session, data: dict, user_id: int):
    task = Task(**data, user_id=user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def list_tasks(db: Session, user_id: int):
    statement = (
        select(Task)
        .where(Task.user_id == user_id)
        .order_by(Task.id.asc())
    )
    return list(db.scalars(statement).all())


def get_task(db: Session, task_id: int, user_id: int):
    statement = select(Task).where(
        Task.id == task_id,
        Task.user_id == user_id,
    )
    return db.scalar(statement)


def update_task(db: Session, task: Task, changes: dict):
    for field, value in changes.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task):
    db.delete(task)
    db.commit()
