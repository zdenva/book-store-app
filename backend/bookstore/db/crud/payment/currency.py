from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_delete,
    instance_update,
)
from bookstore.db.models.payment.currency import Currency
from bookstore.db.schemas.payment.currency import (
    CurrencyCreate,
    CurrencyUpdate,
)


def get_currencies(session: Session, skip: int = 0, limit: int = 100) -> list[Currency]:
    """Get currencies."""
    statement = select(Currency).offset(skip).limit(limit)
    currencies = session.exec(statement).all()
    return currencies


def get_currency(session: Session, currency_id: UUID) -> Currency | None:
    """Get a currency by ID."""
    currency = session.get(Currency, currency_id)
    return currency


def create_currency(session: Session, currency_in: CurrencyCreate) -> Currency:
    """Create a new currency."""
    currency_created = instance_create(
        session=session, model=Currency, schema_in=currency_in
    )
    return currency_created


def update_currency(
    session: Session, currency_id: UUID, currency_in: CurrencyUpdate
) -> Currency | None:
    """Update a currency by ID."""
    currency = get_currency(session=session, currency_id=currency_id)
    currency_updated = instance_update(
        session=session, instance=currency, schema_in=currency_in
    )
    return currency_updated


def delete_currency(session: Session, currency_id: UUID) -> Currency:
    """Delete a currency by ID."""
    currency = get_currency(session=session, currency_id=currency_id)
    currency_deleted = instance_delete(session=session, instance=currency)
    return currency_deleted


def get_count_currencies(session: Session) -> int:
    """Get total count of currency rows in table."""
    count = get_count(session=session, model=Currency)
    return count
