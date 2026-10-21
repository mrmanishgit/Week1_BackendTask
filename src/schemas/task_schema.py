
from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)
