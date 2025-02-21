from typing import Annotated, List
from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse

from backend.db.database import Database, get_db
from backend.models.posts_model import Post, PostBaseResponse

from backend.routers.requests.posts_req import PostCreateRequest, PostUpdateRequest
from backend.routers.responses.posts_res import PostFullResponse 

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=PostBaseResponse)
async def create_post(
    db: Annotated[Database, Depends(get_db)], 
    post: PostCreateRequest
    ):
    db_post = db.create(db_cls=Post, req_obj=post)
    return db_post

@router.get("/", response_model=List[PostBaseResponse])
async def get_all_posts(
    db: Annotated[Database, Depends(get_db)],
    offset: int = 0, 
    limit: int = Query(default=10, le=25)
    ):
    db_posts = db.fetch(db_cls=Post, offset=offset, limit=limit)
    
    return db_posts

@router.get("/{post_id}", response_model=PostFullResponse)
async def get_post(
    db: Annotated[Database, Depends(get_db)],
    post_id: int
    ):
    db_post = db.fetch_one(db_cls=Post, db_id=post_id)
    
    return db_post

@router.put("/{post_id}", response_model=PostBaseResponse)
async def update_post(
    db: Annotated[Database, Depends(get_db)],
    post_id:int, 
    post: PostUpdateRequest
    ):
    db_post = db.update(db_cls=Post, db_id=post_id, req_obj=post)
    return db_post

@router.delete("/{post_id}")
async def delete_post(
    db: Annotated[Database, Depends(get_db)],
    post_id: int
    ):
    db.delete(db_cls=Post, id=post_id)
    return JSONResponse({"ok": True})
