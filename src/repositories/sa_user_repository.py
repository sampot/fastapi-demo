
from typing import List
from domain.entities.user import User
from repositories.sa_base_repository import SABaseRepository

from domain.repositories.user_repository import UserRepository
from repositories.sa_use_case_context import SAUseCaseContext

from sqlalchemy import Table, Column, String
from .database import metadata, mapper_registry


UsersTable = Table(
    "users",
    metadata,
    Column('id', String, primary_key=True),
    Column('username', String(50))
)

# map the entity class to table
mapper_registry.map_imperatively(User, UsersTable)


class SAUserRepository(SABaseRepository, UserRepository):

    def __init__(self, uc_context: SAUseCaseContext) -> None:
        super().__init__(uc_context)

    async def save(self, user: User) -> User:
        self.uc_context.session.add(user)
        return user

    async def get_all(self) -> List[User]:
        return self.uc_context.session.query(User).all()
