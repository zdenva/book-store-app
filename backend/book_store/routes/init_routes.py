from fastapi import APIRouter

from book_store.routes import utils

router = APIRouter()

router.include_router(utils.router)
