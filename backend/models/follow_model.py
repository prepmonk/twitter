from typing import Optional, TYPE_CHECKING
from weakref import ref
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .users_model import User

class FollowBase(SQLModel):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    follow_id: Optional[int] = Field(default=None, primary_key=True)

class Follow(FollowBase, table=True):
    user: "User" = Relationship(back_populates="following")

class FollowBaseResponse(FollowBase):
    pass
