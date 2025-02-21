from sqlmodel import SQLModel

from backend.models.comments_model import CommentBase


class CommentUpdateRequest(SQLModel):
    body: str = None

class CommentCreateRequest(CommentBase):
    pass