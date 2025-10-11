from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.inventory import (
    get_count_inventories,
    get_inventories,
    get_inventory,
    update_inventory,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemes.book.inventory import (
    InventoriesPublic,
    InventoryRead,
    InventoryUpdate,
)

router = APIRouter(prefix="/inventories", tags=["inventories"])


@router.get("/", response_model=InventoriesPublic)
def read_inventories(skip: int = 0, limit: int = 100, session: SessionDep = SessionDep):
    """Get inventories."""
    inventories = get_inventories(session=session, skip=skip, limit=limit)
    count = get_count_inventories(session=session)
    return InventoriesPublic(data=inventories, count=count)


@router.get("/{book_id}", response_model=InventoryRead)
def read_inventory(book_id: str, session: SessionDep = SessionDep):
    """Get an inventory by ID."""
    inventory = get_inventory(session=session, book_id=book_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory


@router.patch("/{book_id}", response_model=InventoryRead)
def edit_inventories(session: SessionDep, book_id: str, inventory_in: InventoryUpdate):
    """
    Update an inventory by ID.
    """
    inventory = update_inventory(
        session=session,
        book_id=book_id,
        quantity=inventory_in.quantity,
    )
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return InventoryRead.from_orm(inventory)
