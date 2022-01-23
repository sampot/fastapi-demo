from pydantic.dataclasses import dataclass

from shared.domain import DomainEntity


@dataclass()
class UserEntity(DomainEntity):
    username: str
