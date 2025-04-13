from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False  # New field to track completion status
    due_date: Optional[datetime] = None  # Optional field to represent the due date

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    status: str
    owner_id: int
    
    class Config:
        orm_mode = True

class TaskUpdate(TaskBase):
    status: Optional[str] = None
    completed: Optional[bool] = None  # Allows updating completion status
    due_date: Optional[datetime] = None  # Allows updating due date
