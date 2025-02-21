from sqlmodel import SQLModel
from backend.models.posts_model import PostBase


class PostCreateRequest(PostBase):
    pass

class PostUpdateRequest(SQLModel):
    body: str = None
