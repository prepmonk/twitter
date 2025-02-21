from typing import List, Optional
from backend.models.users_model import  UserBaseResponse
from backend.models.posts_model import PostBaseResponse

class UserFullResponse(UserBaseResponse):
    posts: Optional[List["PostBaseResponse"]] = None

 