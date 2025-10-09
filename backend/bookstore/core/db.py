from sqlalchemy_utils import create_database, database_exists
from sqlmodel import Session, SQLModel, create_engine

from bookstore.core.config import settings
from bookstore.db.models import *

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
if not database_exists(str(settings.SQLALCHEMY_DATABASE_URI)):
    create_database(str(settings.SQLALCHEMY_DATABASE_URI))


def init_db(session: Session) -> None:
    SQLModel.metadata.create_all(engine)
