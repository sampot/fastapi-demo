from contextvars import ContextVar

from sqlalchemy.orm import Session

from application.context import UseCaseContext

from .database import SessionFactory

_uc_context_storage = ContextVar("use_case_context", default=None)


class SAUseCaseContext(UseCaseContext):
    """SQLAlchemy implementation of UseCaseContext."""

    def __init__(self, session_factory=SessionFactory):
        self.session_factory = session_factory

    @property
    def session(self) -> Session:
        session = _uc_context_storage.get()
        if not session:
            session = self.session_factory()
            _uc_context_storage.set(session)
            print("Session created.")

        return session

    def begin(self) -> Session:
        """begin a transaction"""

        return self.session

    def commit(self):
        """commit the transaction"""
        session = _uc_context_storage.get()
        if not session:
            raise Exception("No associated session.")

        session.commit()
        print('session committed.')

    def rollback(self):
        """roll back the transaction"""
        session = _uc_context_storage.get()
        if not session:
            raise Exception("No associated session.")

        session.rollback()
        print("session rollbacked.")

    def close(self):
        session = _uc_context_storage.get()
        if session:
            _uc_context_storage.set(None)
            session.close()
            print("session closed.")
