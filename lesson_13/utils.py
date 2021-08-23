from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import create_database, database_exists

DB_USER = "manti"
DB_PASSWORD = "manti"
DB_NAME = "manti"
DB_HOST = "localhost"
DB_PORT = 5432
DB_ECHO = True


def setup_db_engine() -> Engine:
    return create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=DB_ECHO,
    )


def create_database_if_not_exists(engine: Engine) -> bool:
    if not database_exists(engine.url):
        create_database(engine.url)
        return True
    return False