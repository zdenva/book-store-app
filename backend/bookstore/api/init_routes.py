from fastapi import APIRouter

from bookstore.api.routes import utils
from bookstore.api.routes.book import authors, genre, language

router = APIRouter()

router.include_router(utils.router)
router.include_router(authors.router)
router.include_router(language.router)
router.include_router(genre.router)
