
from typing import List, Optional
from backend.models.posts_model import PostBaseResponse
from backend.models.comments_model import CommentBaseResponse

from backend.routers.responses.users_res import UserBaseResponse


class PostFullResponse(PostBaseResponse):
    user: "UserBaseResponse" = None
    comments: List["CommentBaseResponse"] = []