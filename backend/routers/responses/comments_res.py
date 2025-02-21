from backend.models.comments_model import CommentBaseResponse

from backend.routers.responses.posts_res import PostBaseResponse


class CommentFullResponse(CommentBaseResponse):
    post: "PostBaseResponse" = None