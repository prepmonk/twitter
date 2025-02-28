from sqlmodel import SQLModel
from backend.models.follow_model import FollowBaseResponse

class FollowUpdateRequest(SQLModel):
    user_id: int = None
    follow_id: int = None

class FollowCreateRequest(FollowBaseResponse):
    user_id: int
    follow_id: int