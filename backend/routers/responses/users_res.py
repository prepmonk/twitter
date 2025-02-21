from typing import List
from backend.models.users_model import  UserBaseResponse
from backend.models.posts_model import PostResponse

class UserFullResponse(UserBaseResponse):
    posts: List["PostResponse"] = []

 