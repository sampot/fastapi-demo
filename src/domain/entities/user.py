from typing import Any, Optional

from cuid import cuid
from pydantic.dataclasses import dataclass

from shared.domain import DomainEntity


@dataclass()
class User(DomainEntity):
    username: str
