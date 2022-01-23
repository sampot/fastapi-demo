from typing import Any, Optional
from shared.domain import DomainEntity
from pydantic.dataclasses import dataclass

from cuid import cuid


@dataclass()
class User(DomainEntity):
    username: str
