from abc import ABC, abstractmethod
from typing import Any


class UseCaseContext(ABC):
    """Interface for interacting with the underlying transactional session."""

    @abstractmethod
    def begin(self):
        """begin a transaction"""
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        """commit the transaction"""
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        """roll back the transaction"""
        raise NotImplementedError

    @abstractmethod
    def close(self):
        """close resources associated with current context."""
        raise NotImplementedError
