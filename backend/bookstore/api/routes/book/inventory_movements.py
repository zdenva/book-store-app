from uuid import UUID

from fastapi import APIRouter, HTTPException

from bookstore.db.crud.book.inventory_movement import (
    create_inventory_movement,
    delete_inventory_movement,
    get_count_inventory_movements,
    get_inventory_movement,
    get_inventory_movements,
    update_inventory_movement,
)
from bookstore.db.deps import SessionDep
from bookstore.db.schemas.book.inventory_movement import (
    InventoryMovementCreate,
    InventoryMovementDelete,
    InventoryMovementRead,
    InventoryMovementsPublic,
    InventoryMovementUpdate,
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
    genre_in: InventoryMovementCreate, session: SessionDep = SessionDep
):
    """
    Create a new inventory movement and return it.
    """
    inventory_movement = create_inventory_movement(session=session, genre_in=genre_in)
    return InventoryMovementRead.from_orm(inventory_movement)


@router.patch("/{inventory_movement_id}", response_model=InventoryMovementRead)
def edit_inventory(
    session: SessionDep,
    inventory_movement_id: UUID,
    inventory_movement_in: InventoryMovementUpdate,
):
    """
    Update an inventory movement by ID.
    """
    inventory_movement = update_inventory_movement(
        session=session,
        inventory_movement_id=inventory_movement_id,
        inventory_movement_in=inventory_movement_in,
    )
    if not inventory_movement:
        raise HTTPException(status_code=404, detail=inventory_movement_404)
    return InventoryMovementRead.from_orm(inventory_movement)


@router.delete("/{inventory_movement_id}", response_model=InventoryMovementDelete)
def remove_inventory_movement(
    inventory_movement_id: UUID, session: SessionDep = SessionDep
):
    """Delete an inventory movement by ID."""
    deleted_inventory_movement = delete_inventory_movement(
        session=session, inventory_movement_id=inventory_movement_id
    )
    if not deleted_inventory_movement:
        raise HTTPException(status_code=404, detail=inventory_movement_404)

    return InventoryMovementDelete(
        id=deleted_inventory_movement.id,
        message="Inventory movement was successfully deleted",
    )
