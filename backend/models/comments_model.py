from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .posts_model import Post

class CommentBase(SQLModel):
    description: str = Field(default="", index=True)
    user_id: int = Field(foreign_key="user.id")
    post_id: int = Field(foreign_key="post.id")

class Comment(CommentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    post: "Post" = Relationship(back_populates="comments")

class CommentBaseResponse(CommentBase):
    id: int