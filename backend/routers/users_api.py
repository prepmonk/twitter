from typing import Annotated, List
from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse

from backend.db.database import Database, get_db

from backend.models.users_model import User, UserBaseResponse
from backend.models.follow_model import Follow

from backend.routers.requests.user_req import UserCreateRequest, UserUpdateRequest
from backend.routers.requests.follow_req import FollowCreateRequest

from backend.routers.responses.users_res import UserFullResponse
from backend.utils.password_helper import hash_password


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserBaseResponse)
async def register_user(db: Annotated[Database, Depends(get_db)], 
                  user: UserCreateRequest):
    extra_data = {"hashed_password": hash_password(user.password)}
    db_user = db.create(db_cls=User, req_obj=user, extra_params=extra_data)
    return db_user

@router.get("/", response_model=List[UserBaseResponse])
async def get_all_users(db: Annotated[Database, Depends(get_db)],
                  offset: int = 0, 
                  limit: int = Query(default=10, le=25)):
    db_users = db.fetch(db_cls=User, offset=offset, limit=limit)
    
    return db_users

@router.get("/{user_id}", response_model=UserFullResponse)
async def get_user(db: Annotated[Database, Depends(get_db)],
             user_id: int):
    db_user = db.fetch_one(db_cls=User, db_id=user_id)
    
    return db_user

@router.put("/{user_id}", response_model=UserBaseResponse)
async def update_user(db: Annotated[Database, Depends(get_db)],
                user_id:int, 
                user: UserUpdateRequest
                ):
    db_user = db.update(db_cls=User, db_id=user_id, req_obj=user)
    return db_user

@router.delete("/{user_id}")
async def delete_user(db: Annotated[Database, Depends(get_db)],
                user_id: int):
    db.delete(db_cls=User, id=user_id)
    return JSONResponse({"ok": True})


#follow

@router.post("/follow", response_model=UserFullResponse)
async def follow_user(
    db: Annotated[Database, Depends(get_db)], 
    follow: FollowCreateRequest
    ):
    user_follow: Follow = db.create(db_cls=Follow, req_obj=follow, extra_params={})
    db_user: User = db.fetch_one(db_cls=User, db_id=follow.user_id)
    db_friend: User = db.fetch_one(db_cls=User, db_id=follow.follow_id)
    db_user.following.append(user_follow)
    db_user = db.save(db_user)
    return db_user