import logging
from typing import List

from dependency_injector.wiring import Provide, inject

from application.containers import Container
from domain.entities.user import UserEntity
from domain.repositories.user_repository import UserRepository

logger = logging.Logger(__name__)


@inject
async def run(
    userRepo: UserRepository = Provide[Container.user_repository],
) -> List[UserEntity]:
    result = await userRepo.get_all()
    return result
