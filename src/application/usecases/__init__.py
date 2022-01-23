from dependency_injector.wiring import Provide, inject

from ..containers import Container
from ..context import UseCaseContext


@inject
def get_uc_context(ctx=Provide[Container.uc_context]) -> UseCaseContext:
    return ctx


def usecase(func):
    """usecase function decorator"""

    async def wrapper(*args, **kwargs):
        # the use-case context must be created first by, e.g., a HTTP middleware.
        ctx = get_uc_context()
        ctx.begin()
        print("Session began.")

        try:
            return await func(*args, **kwargs)
        except:
            ctx.rollback()
            raise
        else:
            ctx.commit()
        finally:
            print("Session closed")
            ctx.close()

    return wrapper
