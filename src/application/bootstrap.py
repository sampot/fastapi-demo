from application import usecases
from application.containers import Container
from application.settings import appSettings
from repositories.database import create_tables

container: Container


def bootstrap():
    """Bootstrap the application by wiring dependencies."""
    container = Container()
    container.config.from_pydantic(appSettings)
    container.wire(packages=[usecases])

    create_tables()
