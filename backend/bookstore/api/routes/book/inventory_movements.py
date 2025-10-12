from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.inventory import update_inventory_quantity
from bookstore.db.crud.book.inventory_movement import (
    create_inventory_movement,
    get_count_inventory_movements,
    get_inventory_movement,
    get_inventory_movements,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemas.book.inventory_movement import (
    InventoryMovementCreate,
    InventoryMovementRead,
    InventoryMovementsPublic,
)

router = APIRouter(prefix="/inventory-movements", tags=["inventory-movements"])

inventory_movement_404 = "Inventory movement not found"


@router.get("/", response_model=InventoryMovementsPublic)
def read_inventory_movements(
    skip: int = 0, limit: int = 100, session: SessionDep = SessionDep
):
    """Get inventory movements."""
    inventory_movements = get_inventory_movements(
        session=session, skip=skip, limit=limit
    )
    count = get_count_inventory_movements(session=session)
    return InventoryMovementsPublic(data=inventory_movements, count=count)


@router.get("/{inventory_movement_id}", response_model=InventoryMovementRead)
def read_inventory_movement(
    inventory_movement_id: UUID, session: SessionDep = SessionDep
):
    """Get an inventory movement by ID."""
    inventory_movement = get_inventory_movement(
        session=session, inventory_movement_id=inventory_movement_id
    )
    if not inventory_movement:
        raise HTTPException(status_code=404, detail=inventory_movement_404)
    return inventory_movement


@router.post("/", response_model=InventoryMovementRead)
def add_inventory_movement(
    inventory_movement_in: InventoryMovementCreate, session: SessionDep = SessionDep
):
    """
    Create a new inventory movement and return it.
    """
    inventory_movement = create_inventory_movement(
        session=session, inventory_movement_in=inventory_movement_in
    )
    if not inventory_movement:
        raise HTTPException(
            status_code=404, detail="Inventory movement wasn't able to be created"
        )
        update_inventory_quantity(
            session=session,
            book_id=inventory_movement.book_id,
            change=inventory_movement.change,
        )
    return InventoryMovementRead.from_orm(inventory_movement)
