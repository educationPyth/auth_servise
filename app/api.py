from fastapi import FastAPI, Body, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.auth.auth_bearer import JWTBearer
from app.hasher.hash_handler import encode_data
from app.model import PostSchema, UserSchema, UserLoginSchema

from typing import Annotated
from app.router.user_router import router as user_router
from app.router.post_router import router as post_router


app = FastAPI()
app.include_router(user_router)
app.include_router(post_router)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любого источника (можно ограничить по необходимости)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы
    allow_headers=["*"],  # Разрешает все заголовки
)

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your blog!"}
