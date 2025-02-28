from typing import Annotated, List
from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse

from backend.db.database import Database, get_db
from backend.models.emotions_model import Emotion, EmotionBaseResponse
from backend.routers.requests.emotions_req import EmotionCreateRequest, EmotionUpdateRequest
from backend.routers.responses.emotions_res import EmotionFullResponse

router = APIRouter(prefix="/emotions", tags=["emotions"])

@router.post("/", response_model=EmotionBaseResponse)
async def create_emotion(
    db: Annotated[Database, Depends(get_db)], 
    emotion: EmotionCreateRequest
    ):
    db_emotion = db.create(db_cls=Emotion, req_obj=emotion)
    return db_emotion

@router.get("/", response_model=List[EmotionBaseResponse])
async def emotions( 
    db: Annotated[Database, Depends(get_db)],
    offset: int = 0, 
    limit: int = Query(default=10, le=25)
    ):
    emotions = db.fetch(db_cls=Emotion, offset=offset, limit=limit)
    
    return emotions

@router.get("/{emotion_id}", response_model=EmotionFullResponse)
async def get_emotion(
    db: Annotated[Database, Depends(get_db)],
    emotion_id: int
    ):
    db_emotion = db.fetch_one(db_cls=Emotion, db_id=emotion_id)
    
    return db_emotion

@router.put("/{emotion_id}", response_model=EmotionBaseResponse)
async def update_emotion(
    db: Annotated[Database, Depends(get_db)],
    emotion_id:int, 
    emotion: EmotionUpdateRequest
    ):
    db_emotion = db.update(db_cls=Emotion, db_id=emotion_id, req_obj=emotion)
    return db_emotion

@router.delete("/{emotion_id}")
async def delete_emotion(
    db: Annotated[Database, Depends(get_db)],
    emotion_id: int
    ):
    db.delete(db_cls=Emotion, id=emotion_id)
    return JSONResponse({"ok": True})
