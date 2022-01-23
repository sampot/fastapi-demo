from abc import ABC
from typing import Any, Dict, Optional

from pydantic.dataclasses import dataclass


@dataclass
class DomainEntity:
    id: str
    org_id: Optional[str]


@dataclass
class ValueObject(object):
    pass


@dataclass
class DomainEvent(object):
    id: str
    timestamp: int
    type: str
    payload: Optional[Dict[Any, Any]]


class DomainError(Exception):
    pass


class Repository(ABC):
    pass


class DomainService(ABC):
    pass
