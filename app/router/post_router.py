from fastapi import APIRouter, Depends
from typing import Annotated

from app.auth.auth_bearer import JWTBearer
from app.model import PostSchema

router = APIRouter(
    prefix="/posts"
)

posts = []


@router.get("", tags=["posts"])
async def get_posts() -> dict:
    return {"data": posts}


@router.get("/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@router.post("", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: Annotated[PostSchema, Depends()]) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }
