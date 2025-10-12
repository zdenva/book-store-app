from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.book.inventory import update_inventory_quantity
from bookstore.db.crud.utils import (
    check_instance_exists,
    get_count,
    instance_create,
    instance_delete,
)
from bookstore.db.models.book.book import Book
from bookstore.db.models.book.inventory_movement import InventoryMovement
from bookstore.db.schemas.book.inventory_movement import (
    InventoryMovementCreate,
)


def get_inventory_movements(
    session: Session, skip: int = 0, limit: int = 100
) -> list[InventoryMovement]:
    """Get inventory movements."""
    statement = select(InventoryMovement).offset(skip).limit(limit)
    inventory_movements = session.exec(statement).all()
    return inventory_movements


def get_inventory_movement(
    session: Session, inventory_movement: UUID
) -> InventoryMovement | None:
    """Get an inventory movement by ID."""
    inventory_movement = session.get(InventoryMovement, inventory_movement)
    return inventory_movement


def create_inventory_movement(
    session: Session, inventory_movement_in: InventoryMovementCreate
) -> InventoryMovement | None:
    """Create a new inventory movement."""
    if not check_instance_exists(
        session=session, model=Book, instance_id=inventory_movement_in.book_id
    ):
        return None
    inventory_movement_created = instance_create(
        session=session, model=InventoryMovement, schema_in=inventory_movement_in
    )
    update_inventory_quantity(
        session=session,
        book_id=inventory_movement_in.book_id,
        change=inventory_movement_in.change,
    )
    return inventory_movement_created


def delete_inventory_movement(
    session: Session, inventory_movement: UUID
) -> InventoryMovement:
    """Delete an inventory movement by ID."""
    inventory_movement = get_inventory_movement(
        session=session, inventory_movement=inventory_movement
    )
    inventory_movement_deleted = instance_delete(
        session=Session, instance=inventory_movement
    )
    return inventory_movement_deleted


def get_count_inventory_movements(session: Session) -> int:
    """Get total count of inventory movements rows in table."""
    count = get_count(session=session, model=InventoryMovement)
    return count
