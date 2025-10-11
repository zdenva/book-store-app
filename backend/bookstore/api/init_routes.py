from fastapi import APIRouter

from bookstore.api.routes import utils
from bookstore.api.routes.book import (
    authors,
    book_prices,
    genre,
    inventories,
    inventory_movements,
    language,
    publishers,
)
from bookstore.api.routes.payment import currency

router = APIRouter()

router.include_router(utils.router)
router.include_router(authors.router)
router.include_router(language.router)
router.include_router(genre.router)
router.include_router(publishers.router)
router.include_router(inventories.router)
router.include_router(book_prices.router)
router.include_router(inventory_movements.router)
router.include_router(currency.router)
