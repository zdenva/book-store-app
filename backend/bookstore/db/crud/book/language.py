from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_delete,
    instance_update,
)
from bookstore.db.models.book.language import Language
from bookstore.db.schemas.book.language import (
    LanguageCreate,
    LanguageUpdate,
)


def get_languages(session: Session, skip: int = 0, limit: int = 100) -> list[Language]:
    """Get languages."""
    statement = select(Language).offset(skip).limit(limit)
    return session.exec(statement).all()


def get_language(session: Session, language_id: UUID) -> Language | None:
    """Get a language by ID."""
    language = session.get(Language, language_id)
    return language


def create_language(session: Session, language_in: LanguageCreate) -> Language:
    """Create a new language."""
    language_created = instance_create(
        session=session, model=Language, schema_in=language_in
    )
    return language_created


def update_language(
    session: Session, language_id: UUID, language_in: LanguageUpdate
) -> Language | None:
    """Update a language by ID."""
    language = get_language(session=session, language_id=language_id)
    language_updated = instance_update(
        session=session, instance=language, schema_in=language_in
    )
    return language_updated


def delete_language(session: Session, language_id: UUID) -> Language:
    """Delete a language by ID."""
    language = get_language(session=session, language_id=language_id)
    language_deleted = instance_delete(session=session, instance=language)
    return language_deleted


def get_count_languages(session: Session) -> int:
    """Get total count of genre rows in table."""
    count = get_count(session=session, model=Language)
    return count
