from contextlib import asynccontextmanager
import  uvicorn
from fastapi import FastAPI
from backend.db.database import create_db_tables, drop_db_tables
from backend.routers import comments_api, posts_api, users_api, emotions_api

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_tables()
    print("Before Lifespan")
    yield
    print("After Lifespan")
    drop_db_tables()

app = FastAPI(lifespan=lifespan)

app.include_router(users_api.router)
app.include_router(posts_api.router)
app.include_router(comments_api.router)
app.include_router(emotions_api.router)

@app.get("/")
async def index():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run(app="app", host="0.0.0.0", port="8001", reload=True)
