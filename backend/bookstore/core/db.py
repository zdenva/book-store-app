from sqlalchemy_utils import create_database, database_exists
from sqlmodel import Session, SQLModel, create_engine

from bookstore.db.models import *  # noqa: F403
from bookstore.core.config import settings

if not database_exists(str(settings.SQLALCHEMY_DATABASE_URI)):
    create_database(str(settings.SQLALCHEMY_DATABASE_URI))
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def init_db(session: Session) -> None:
    SQLModel.metadata.create_all(engine)
