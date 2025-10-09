from fastapi import APIRouter

from bookstore.api.routes import authors, utils

router = APIRouter()

router.include_router(utils.router)
router.include_router(authors.router)
