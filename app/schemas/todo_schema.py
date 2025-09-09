from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class TodoStatus(str, Enum):
    pending = "pending"
    completed = "completed"

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TodoStatus] = None

class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TodoStatus
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
