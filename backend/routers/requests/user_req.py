from sqlmodel import SQLModel
from backend.models.users_model import UserBase

class UserUpdateRequest(SQLModel):
    first_name: str = None
    last_name: str = None
    username: str = None
    password: str = None

class UserCreateRequest(UserBase):
    password: str