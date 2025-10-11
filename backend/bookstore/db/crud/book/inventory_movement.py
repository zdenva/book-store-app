from uuid import UUID

from sqlmodel import Session, select

from bookstore.db.crud.utils import (
    get_count,
    instance_create,
    instance_delete,
    instance_update,
)
from bookstore.db.models.book.inventory_movement import InventoryMovement
from bookstore.db.schemas.book.inventory_movement import (
    InventoryMovementCreate,
    InventoryMovementUpdate,
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
    inventory_movement_created = instance_create(
        session=session, model=InventoryMovement, schema_in=inventory_movement_in
    )
    return inventory_movement_created


def update_inventory_movement(
    session: Session,
    inventory_movement: UUID,
    inventory_movement_in=InventoryMovementUpdate,
) -> InventoryMovement | None:
    """Update an inventory movement by ID."""
    inventory_movement = get_inventory_movement(
        session=session, inventory_movement=inventory_movement
    )
    inventory_movement_updated = instance_update(
        session=Session, instance=inventory_movement, schema_in=inventory_movement_in
    )
    return inventory_movement_updated


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
