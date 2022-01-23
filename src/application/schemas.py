from typing import Any, List

from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str


class ListResut(BaseModel):
    data: List[Any] = []
    object: str = "list"
    next_id: str = ""
    num_of_items: int = 0


class ErrorResult(BaseModel):
    error: str
    detail: Any
