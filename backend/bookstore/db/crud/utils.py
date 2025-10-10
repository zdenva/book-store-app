from sqlmodel import Session, SQLModel, func, select


def get_count(session: Session, model: SQLModel) -> int:
    """Get total row count for the given SQLModel."""
    count_statement = select(func.count()).select_from(model)
    count = session.exec(count_statement).first()
    return count or 0
