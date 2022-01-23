from fastapi import FastAPI

from application.bootstrap import bootstrap

from .endpoints import auth, root, users

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
