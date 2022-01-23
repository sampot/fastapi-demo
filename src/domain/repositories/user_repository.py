from abc import abstractmethod
from typing import List

from domain.entities.user import User
from shared.domain import Repository


class UserRepository(Repository):
    """Contractual interface for UserRepository"""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    async def save(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[User]:
        raise NotImplementedError
