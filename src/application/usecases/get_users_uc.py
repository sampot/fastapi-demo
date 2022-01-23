from typing import List
from application.containers import Container
from dependency_injector.wiring import Provide, inject
import logging
from pydantic import BaseModel
from cuid import cuid
from domain.entities.user import User

from domain.repositories.user_repository import UserRepository
from application.usecases import usecase

logger = logging.Logger(__name__)


@usecase
@inject
async def run(userRepo: UserRepository = Provide[Container.user_repository]) -> List[User]:
    result = await userRepo.get_all()
    return result
