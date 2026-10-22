
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


TaskStatus = Literal["PENDING", "IN_PROGRESS", "COMPLETED"]
TaskPriority = Literal["LOW", "MEDIUM", "HIGH", "URGENT"]


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = None
    status: TaskStatus = "PENDING"
    priority: TaskPriority = "MEDIUM"
    due_date: datetime | None = None


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = None
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    due_date: datetime | None = None

    @model_validator(mode="after")
    def validate_not_empty(self):
        if not self.model_fields_set:
            raise ValueError("Provide at least one field to update")
        return self


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    completed: bool
    status: TaskStatus
    priority: TaskPriority
    due_date: datetime | None
    user_id: int
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None
