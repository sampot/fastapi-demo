import logging

from cuid import cuid
from dependency_injector.wiring import Provide, inject
from pydantic import BaseModel

from application.containers import Container
from domain.entities.user import UserEntity
from domain.repositories.user_repository import UserRepository

logger = logging.Logger(__name__)


class CreateUserRequest(BaseModel):
    username: str


class CreateUserResponse(BaseModel):
    id: str
    username: str


@inject
async def run(
    req: CreateUserRequest,
    userRepo: UserRepository = Provide[Container.user_repository],
) -> UserEntity:
    result = await userRepo.save(UserEntity(**dict(req), id=cuid(), org_id="default"))
    return result
