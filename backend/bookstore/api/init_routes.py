from fastapi import APIRouter

from bookstore.api.routes import utils
from bookstore.api.routes.book import authors, genre, inventories, language, publishers

router = APIRouter()

router.include_router(utils.router)
router.include_router(authors.router)
router.include_router(language.router)
router.include_router(genre.router)
router.include_router(publishers.router)
router.include_router(inventories.router)
