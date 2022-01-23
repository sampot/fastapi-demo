import logging

from cuid import cuid
from dependency_injector.wiring import Provide, inject
from pydantic import BaseModel

from application.containers import Container
from application.usecases import usecase
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

logger = logging.Logger(__name__)


class CreateUserRequest(BaseModel):
    username: str


class CreateUserResponse(BaseModel):
    id: str
    username: str


@usecase
@inject
async def run(
    req: CreateUserRequest,
    userRepo: UserRepository = Provide[Container.user_repository],
) -> User:
    logger.info("create user")
    result = await userRepo.save(User(**dict(req), id=cuid(), org_id=None))
    print(f"result: {result}")
    return result
