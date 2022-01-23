from tkinter import E
from fastapi import Request
from ..app import app
from application.usecases import get_uc_context


@app.middleware("http")
async def use_case_context(request: Request, call_next):
    print("context middleware")
    uc_ctx = get_uc_context()
    uc_ctx.begin()
    error = False
    try:
        return await call_next(request)
    except Exception as e:
        error = True
        uc_ctx.rollback()
        raise E
    finally:
        if not error:
            uc_ctx.commit()
        uc_ctx.close()
