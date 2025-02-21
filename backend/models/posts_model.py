from typing import List, Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .users_model import User
    from .comments_model import Comment

class PostBase(SQLModel):
    body: str = Field(index=True)
    user_id: int = Field(foreign_key="user.id")

class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    user: "User" = Relationship(back_populates="posts")
    comments: List["Comment"] = Relationship(back_populates="post")

class PostBaseResponse(PostBase):
    id: int




    