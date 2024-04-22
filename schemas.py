from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from models import User


class UserSchema(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    registration_time: Optional[datetime] = None

    class Config:
        orm_mode = True

    @classmethod
    def create_user(cls, data: dict) -> User:
        return User(**data)


class UpdateUserSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None