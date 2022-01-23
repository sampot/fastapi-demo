import uvicorn

from .app import app
from application.bootstrap import bootstrap
from .middlewares import context_middleware

# bootstrap application
bootstrap()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
