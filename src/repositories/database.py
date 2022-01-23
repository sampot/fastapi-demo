from click import echo
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, registry

SQLALCHEMY_DATABASE_URL = "sqlite:///"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args={
        "check_same_thread": False,
    },
)


metadata = MetaData()

mapper_registry = registry(metadata)

SessionFactory = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


def create_tables():
    metadata.create_all(engine)
