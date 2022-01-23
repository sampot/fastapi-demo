import logging
from typing import List

from cuid import cuid
from dependency_injector.wiring import Provide, inject
from pydantic import BaseModel

from application.containers import Container
from application.usecases import usecase
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

logger = logging.Logger(__name__)


@usecase
@inject
async def run(
    userRepo: UserRepository = Provide[Container.user_repository],
) -> List[User]:
    result = await userRepo.get_all()
    return result
