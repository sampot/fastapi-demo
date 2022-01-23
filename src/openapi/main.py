import uvicorn

from application.bootstrap import bootstrap

from .app import app
from .middlewares import context_middleware as _

# bootstrap application
bootstrap()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
