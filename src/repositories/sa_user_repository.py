from typing import List

from sqlalchemy import Column, String, Table

from domain.entities.user import UserEntity
from domain.repositories.user_repository import UserRepository
from repositories.sa_base_repository import SABaseRepository
from repositories.sa_use_case_context import SAUseCaseContext

from .database import mapper_registry, metadata

UsersTable = Table(
    "users",
    metadata,
    Column("id", String, primary_key=True),
    Column("org_id", String, nullable=True),
    Column("username", String(50)),
)

# map the entity class to table
mapper_registry.map_imperatively(UserEntity, UsersTable)


class SAUserRepository(SABaseRepository, UserRepository):
    def __init__(self, uc_context: SAUseCaseContext) -> None:
        super().__init__(uc_context)

    async def save(self, user: UserEntity) -> UserEntity:
        self.uc_context.session.add(user)
        return user

    async def get_all(self) -> List[UserEntity]:
        res = self.uc_context.session.query(UserEntity).all()
        return res
