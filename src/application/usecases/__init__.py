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
        print("Session began.")

        try:
            res = await func(*args, **kwargs)
            ctx.commit()
            return res

        except Exception as e:
            ctx.rollback()
            raise e
        finally:
            print("Session closed")
            ctx.close()

    return wrapper
