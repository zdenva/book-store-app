from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import get_count
from bookstore.db.models.book.inventory import Inventory
from bookstore.db.schemes.book.inventory import InventoryCreate


def get_inventories(
    session: Session, skip: int = 0, limit: int = 100
) -> list[Inventory]:
    """Get inventories."""
    statement = select(Inventory).offset(skip).limit(limit)
    return session.exec(statement).all()


def get_inventory(session: Session, book_id: UUID) -> Inventory | None:
    """Get an inventory by ID."""
    inventory = session.get(Inventory, book_id)
    if not inventory:
        return None
    return inventory


def create_inventory(session: Session, inventory_in: InventoryCreate) -> Inventory:
    """Create a new inventory."""
    inventory = Inventory(**inventory_in.dict())

    session.add(inventory)
    session.commit()
    session.refresh(inventory)

    return inventory


def update_inventory(session: Session, book_id: str, quantity: int) -> Inventory | None:
    """Update an inventory by ID."""
    inventory = get_inventory(session=session, book_id=book_id)
    if not inventory:
        return None
    inventory.quantity = quantity
    session.add(inventory)
    session.commit()
    session.refresh(inventory)
    return inventory


def delete_inventory(session: Session, book_id) -> Inventory:
    """Delete an inventory by ID."""
    inventory = get_inventory(session=session, book_id=book_id)
    if not inventory:
        return None
    session.delete(inventory)
    session.commit()
    return inventory


def get_count_inventories(session: Session) -> int:
    """Get total count of inventory rows in table."""
    return get_count(session=session, model=Inventory)
