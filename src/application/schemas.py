from pydantic import BaseModel
from typing import Any, List


class ListResut(BaseModel):
    data: List[Any] = []
    object: str = 'list'
    next_id: str = ""
    num_of_items: int = 0


class ErrorResult(BaseModel):
    error: str
    detail: Any
