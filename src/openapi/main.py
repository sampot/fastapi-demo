from .endpoints import auth, users, root
import uvicorn
from fastapi import FastAPI
from application.bootstrap import bootstrap

title = "Example API"

description = """
Example OpenAPI 1.0.
"""

tags_metadata = [
    {
        "name": "Authentication",
        "description": "Endpoint for authenticating users.",
    },
    {
        "name": "Users",
        "description": "User management.",
    },
]

# bootstrap application
bootstrap()

app = FastAPI(
    title=title,
    description=description,
    version="1.0",
    openapi_tags=tags_metadata,
    redoc_url=None,
)


app.include_router(auth.router)
app.include_router(users.router)

app.include_router(root.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
