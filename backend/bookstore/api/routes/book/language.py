from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.language import (
    create_language,
    delete_language,
    get_count_languages,
    get_language,
    get_languages,
    update_language,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemes.book.language import (
    LanguageCreate,
    LanguageDelete,
    LanguageRead,
    LanguagesPublic,
    LanguageUpdate,
)

router = APIRouter(prefix="/languages", tags=["languages"])


@router.get("/", response_model=LanguagesPublic)
def read_languages(skip: int = 0, limit: int = 100, session: SessionDep = SessionDep):
    """Get languages."""
    languages = get_languages(session=session, skip=skip, limit=limit)
    count = get_count_languages(session=session)
    return LanguagesPublic(data=languages, count=count)


@router.get("/{language_id}", response_model=LanguageRead)
def read_language(language_id: UUID, session: SessionDep = SessionDep):
    """Get an language by ID."""
    language = get_language(session=session, language_id=language_id)
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    return language


@router.post("/", response_model=LanguageRead)
def add_language(language_in: LanguageCreate, session: SessionDep = SessionDep):
    """
    Create a new language and return it.
    """
    language = create_language(session=session, language_in=language_in)
    return LanguageRead.from_orm(language)


@router.patch("/{language_id}", response_model=LanguageRead)
def edit_language(session: SessionDep, language_id: UUID, language_in: LanguageUpdate):
    """
    Update an language by ID.
    """
    language = update_language(
        session=session, language_id=language_id, language_in=language_in
    )
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    return LanguageRead.from_orm(language)


@router.delete("/{language_id}", response_model=LanguageDelete)
def remove_language(language_id: UUID, session: SessionDep = SessionDep):
    """Delete an language by ID."""
    deleted_language = delete_language(session=session, language_id=language_id)
    if not deleted_language:
        raise HTTPException(status_code=404, detail="Language not found")

    return LanguageDelete(
        id=deleted_language.id,
        message=f"Language '{deleted_language.name}' was successfully deleted",
    )
