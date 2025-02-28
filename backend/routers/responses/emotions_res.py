from backend.models.emotions_model import EmotionBaseResponse
from backend.routers.responses.posts_res import PostBaseResponse


class EmotionFullResponse(EmotionBaseResponse):
    post: "PostBaseResponse" = None