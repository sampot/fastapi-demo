

from application.containers import Container
from application import context, usecases
from repositories.database import create_engine, create_tables

container: Container


def bootstrap():
    """ Bootstrap the application by wiring dependencies. """
    container = Container()
    container.wire(packages=[usecases, context])

    create_tables()
