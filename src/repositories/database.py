from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import registry, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./db/example.db"

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
