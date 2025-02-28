from enum import Enum
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .posts_model import Post

class EmotionType(Enum):
    NONE = None
    THUMBS_UP = "thumbs_up"
    THUMBS_DOWN = "thumbs_down"


class EmotionBase(SQLModel):
    emotion: EmotionType = Field(default=EmotionType.NONE, index=True)
    user_id: int = Field(foreign_key="user.id")
    post_id: int = Field(foreign_key="post.id")

class Emotion(EmotionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    post: "Post" = Relationship(back_populates="emotions")

class EmotionBaseResponse(EmotionBase):
    id: int