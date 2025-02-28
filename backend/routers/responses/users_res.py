from typing import List
from backend.models.users_model import UserBaseResponse
from backend.models.posts_model import PostBaseResponse
from backend.models.follow_model import FollowBaseResponse

class UserFullResponse(UserBaseResponse):
    posts: List["PostBaseResponse"] = []
    following: List["FollowBaseResponse"] = []

 