from fastapi import APIRouter

from bookstore.api.routes import authors, genre, language, utils

router = APIRouter()

router.include_router(utils.router)
router.include_router(authors.router)
router.include_router(language.router)
router.include_router(genre.router)
