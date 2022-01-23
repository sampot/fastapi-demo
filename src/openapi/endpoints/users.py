from typing import List

from fastapi import APIRouter

from application.usecases import create_user_uc, get_users_uc
from domain.entities.user import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[User])
async def get_users():
    try:
        return await get_users_uc.run()
    except:
        raise


@router.post("/", response_model=create_user_uc.CreateUserResponse)
async def create_user(req: create_user_uc.CreateUserRequest):
    try:
        return await create_user_uc.run(req)
    except:
        # TODO: map errors to HTTPExceptions
        raise
