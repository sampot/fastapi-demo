from typing import List

from fastapi import APIRouter

from application.schemas import User
from application.usecases import create_user_uc, get_users_uc

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[User])
async def get_users():
    return await get_users_uc.run()


@router.post("/", response_model=create_user_uc.CreateUserResponse)
async def create_user(req: create_user_uc.CreateUserRequest):
    return await create_user_uc.run(req)
