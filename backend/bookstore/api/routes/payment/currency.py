from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.payment.currency import (
    create_currency,
    delete_currency,
    get_count_currencies,
    get_currencies,
    get_currency,
    update_currency,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemas.payment.currency import (
    CurrenciesPublic,
    CurrencyCreate,
    CurrencyDelete,
    CurrencyRead,
    CurrencyUpdate,
)

router = APIRouter(prefix="/currencies", tags=["currencies"])
currency_404 = "Currency not found"


@router.get("/", response_model=CurrenciesPublic)
def read_currencies(skip: int = 0, limit: int = 100, session: SessionDep = SessionDep):
    """Get currencies."""
    currencies = get_currencies(session=session, skip=skip, limit=limit)
    count = get_count_currencies(session=session)
    return CurrenciesPublic(data=currencies, count=count)


@router.get("/{currency_id}", response_model=CurrencyRead)
def read_currency(currency_id: UUID, session: SessionDep = SessionDep):
    """Get a currency by ID."""
    currency = get_currency(session=session, currency_id=currency_id)
    if not currency:
        raise HTTPException(status_code=404, detail=currency_404)
    return currency


@router.post("/", response_model=CurrencyRead)
def add_currency(currency_in: CurrencyCreate, session: SessionDep = SessionDep):
    """
    Create a new currency and return it.
    """
    currency = create_currency(session=session, currency_in=currency_in)
    return CurrencyRead.from_orm(currency)


@router.patch("/{currency_id}", response_model=CurrencyRead)
def edit_currency(session: SessionDep, currency_id: UUID, currency_in: CurrencyUpdate):
    """
    Update a currency by ID.
    """
    currency = update_currency(
        session=session, currency_id=currency_id, currency_in=currency_in
    )
    if not currency:
        raise HTTPException(status_code=404, detail=currency_404)
    return CurrencyRead.from_orm(currency)


@router.delete("/{currency_id}", response_model=CurrencyDelete)
def remove_currency(currency_id: UUID, session: SessionDep = SessionDep):
    """Delete a currency by ID."""
    deleted_currency = delete_currency(session=session, currency_id=currency_id)
    if not deleted_currency:
        raise HTTPException(status_code=404, detail=currency_404)

    return CurrencyDelete(
        id=deleted_currency.id,
        message="Currency was successfully deleted",
    )
