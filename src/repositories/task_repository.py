
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.task import Task
from src.schemas.task_schema import TaskCreate, TaskUpdate


def create_task(db: Session, data: TaskCreate) -> Task:
    task = Task(
        title=data.title,
        completed=data.completed,
    )

    try:
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    except Exception:
        db.rollback()
        raise


def get_all_tasks(db: Session) -> list[Task]:
    statement = select(Task).order_by(Task.id)
    return list(db.scalars(statement).all())


def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return db.get(Task, task_id)


def update_task(
    db: Session,
    task: Task,
    data: TaskUpdate,
) -> Task:
    task.title = data.title
    task.completed = data.completed

    try:
        db.commit()
        db.refresh(task)
        return task
    except Exception:
        db.rollback()
        raise


def delete_task(db: Session, task: Task) -> None:
    try:
        db.delete(task)
        db.commit()
    except Exception:
        db.rollback()
        raise
