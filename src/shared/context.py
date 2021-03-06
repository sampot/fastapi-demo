from collections import UserDict
from contextvars import ContextVar, copy_context
from typing import Any, Dict

_request_scope_context_storage: ContextVar[Dict[Any, Any]] = ContextVar(
    "example_context", dict()
)


class ContextNotExistError(Exception):
    pass


class _Context(UserDict):
    """
    A mapping with dict-like interface.
    It is using request context as a data store. Can be used only if context
    has been created in the middleware.
    """

    def __init__(self, *args: Any, **kwargs: Any):  # noqa
        # not calling super on purpose
        if args or kwargs:
            raise Exception("Can't instantiate with attributes")

    @property
    def data(self) -> dict:  # type: ignore
        """
        Dump this to json.
        Object itself it not serializable.
        """
        try:
            return _request_scope_context_storage.get()
        except LookupError:
            raise ContextNotExistError

    def exists(self) -> bool:
        return _request_scope_context_storage in copy_context()

    def copy(self) -> dict:  # type: ignore
        """Read only context data."""
        import copy

        return copy.copy(self.data)


context = _Context()
