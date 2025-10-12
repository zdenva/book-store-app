from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_update,
)
from bookstore.db.models.book.inventory import Inventory
from bookstore.db.schemas.book.inventory import InventoryCreate, InventoryUpdate


def get_inventories(
    session: Session, skip: int = 0, limit: int = 100
) -> list[Inventory]:
    """Get inventories."""
    statement = select(Inventory).offset(skip).limit(limit)
    inventories = session.exec(statement).all()
    return inventories


def get_inventory(session: Session, book_id: UUID) -> Inventory | None:
    """Get an inventory by ID."""
    inventory = session.get(Inventory, book_id)
    return inventory


def create_inventory(
    session: Session, inventory_in: InventoryCreate
) -> Inventory | None:
    """Create a new inventory."""
    inventory_created = instance_create(
        session=session, model=Inventory, schema_in=inventory_in
    )
    return inventory_created


def update_inventory_quantity(session: Session, book_id: UUID, change: int):
    """Update quantity."""
    inventory = get_inventory(session=session, book_id=book_id)
    calculated_change = inventory.quantity + change
    inventory_in = InventoryUpdate(book_id=book_id, quantity=calculated_change)
    update_inventory(session=session, book_id=book_id, inventory_in=inventory_in)


def update_inventory(
    session: Session, book_id: UUID, inventory_in=InventoryUpdate
) -> Inventory | None:
    """Update an inventory by ID."""
    inventory = get_inventory(session=session, book_id=book_id)
    inventory_updated = instance_update(
        session=session, instance=inventory, schema_in=inventory_in
    )
    return inventory_updated


def get_count_inventories(session: Session) -> int:
    """Get total count of inventory rows in table."""
    count = get_count(session=session, model=Inventory)
    return count
