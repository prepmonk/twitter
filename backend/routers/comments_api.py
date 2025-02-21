from typing import Annotated, List
from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse

from backend.db.database import Database, get_db
from backend.models.comments_model import Comment, CommentBaseResponse
from backend.routers.requests.comments_req import CommentCreateRequest, CommentUpdateRequest
from backend.routers.responses.comments_res import CommentFullResponse

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/", response_model=CommentBaseResponse)
async def create_comment(
    db: Annotated[Database, Depends(get_db)], 
    comment: CommentCreateRequest
    ):
    db_comment = db.create(db_cls=Comment, req_obj=comment)
    return db_comment

@router.get("/", response_model=List[CommentBaseResponse])
async def get_all_comments( 
    db: Annotated[Database, Depends(get_db)],
    offset: int = 0, 
    limit: int = Query(default=10, le=25)
    ):
    db_comments = db.fetch(db_cls=Comment, offset=offset, limit=limit)
    
    return db_comments

@router.get("/{comment_id}", response_model=CommentFullResponse)
async def get_comment(
    db: Annotated[Database, Depends(get_db)],
    comment_id: int
    ):
    db_comment = db.fetch_one(db_cls=Comment, db_id=comment_id)
    
    return db_comment

@router.put("/{comment_id}", response_model=CommentBaseResponse)
async def update_comment(
    db: Annotated[Database, Depends(get_db)],
    comment_id:int, 
    comment: CommentUpdateRequest
    ):
    db_comment = db.update(db_cls=Comment, db_id=comment_id, req_obj=comment)
    return db_comment

@router.delete("/{comment_id}")
async def delete_comment(
    db: Annotated[Database, Depends(get_db)],
    comment_id: int
    ):
    db.delete(db_cls=Comment, id=comment_id)
    return JSONResponse({"ok": True})
