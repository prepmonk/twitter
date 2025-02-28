from sqlmodel import SQLModel

from backend.models.emotions_model import EmotionBase


class EmotionUpdateRequest(SQLModel):
    body: str = None

class EmotionCreateRequest(EmotionBase):
    pass