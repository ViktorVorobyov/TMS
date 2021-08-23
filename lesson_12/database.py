from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

DB_USER = "manti"
DB_PASSWORD = "manti"
DB_NAME = "manti"
DB_ECHO = True


def create_connection():
    engine = create_engine(
       f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=DB_ECHO,
    )
    if not database_exists(engine.url):
        create_database(engine.url)
    return engine