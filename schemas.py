from typing import Optional
from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    text: str = Field(min_length=1, max_length=200)
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    text: Optional[str] = None
    completed: Optional[bool] = None


class TodoOut(TodoBase):
    id: int

    class Config:
        from_attributes = True
