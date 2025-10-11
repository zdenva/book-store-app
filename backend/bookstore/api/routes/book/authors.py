from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.author import (
    create_author,
    delete_author,
    get_author,
    get_authors,
    get_count_authors,
    update_author,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemes.book.author import (
    AuthorCreate,
    AuthorDelete,
    AuthorRead,
    AuthorsPublic,
    AuthorUpdate,
)

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("/", response_model=AuthorsPublic)
def read_authors(skip: int = 0, limit: int = 100, session: SessionDep = SessionDep):
    """Get authors."""
    authors = get_authors(session=session, skip=skip, limit=limit)
    count = get_count_authors(session=session)
    return AuthorsPublic(data=authors, count=count)


@router.get("/{author_id}", response_model=AuthorRead)
def read_author(author_id: UUID, session: SessionDep = SessionDep):
    """Get an author by ID."""
    author = get_author(session=session, author_id=author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/", response_model=AuthorRead)
def add_author(author_in: AuthorCreate, session: SessionDep = SessionDep):
    """
    Create a new author and return it.
    """
    author = create_author(session=session, author_in=author_in)
    return AuthorRead.from_orm(author)


@router.patch("/{author_id}", response_model=AuthorRead)
def edit_author(session: SessionDep, author_id: UUID, author_in: AuthorUpdate):
    """
    Update an author by ID.
    """
    author = update_author(session=session, author_id=author_id, author_in=author_in)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return AuthorRead.from_orm(author)


@router.delete("/{author_id}", response_model=AuthorDelete)
def remove_author(author_id: UUID, session: SessionDep = SessionDep):
    """Delete an author by ID."""
    deleted_author = delete_author(session=session, author_id=author_id)
    if not deleted_author:
        raise HTTPException(status_code=404, detail="Author not found")

    return AuthorDelete(
        id=deleted_author.id,
        message=f"Author '{deleted_author.first_name} {deleted_author.last_name}' was successfully deleted",
    )
