from uuid import UUID

from pydantic import BaseModel
from sqlmodel import Session, SQLModel, func, select
from sqlalchemy import exists


def get_count(session: Session, model: SQLModel) -> int:
    """Get total row count for the given SQLModel."""
    count_statement = select(func.count()).select_from(model)
    count = session.exec(count_statement).first()
    return count or 0


def instance_create(session: Session, model: SQLModel, schema_in: BaseModel):
    """Create a new ORM instance from a Pydantic model and persist it."""
    instance = model(**schema_in.model_dump())
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


def instance_update(session: Session, instance, schema_in: BaseModel):
    """Update an existing ORM instance with values from a Pydantic model."""
    if instance is None:
        return None

    for key, value in schema_in.model_dump(exclude_none=True).items():
        setattr(instance, key, value)
    session.commit()
    session.refresh(instance)
    return instance


def instance_delete(session: Session, instance):
    """Delete ORM instance."""
    if instance is None:
        return None

    session.delete(instance)
    session.commit()
    return instance


def check_instance_exists(session: Session, model: SQLModel, instance_id: UUID) -> bool:
    """Check if instance exists"""
    statement = select(exists().where(model.id == instance_id))
    result = session.exec(statement).one()
    return result
