from fastapi import APIRouter

from bookstore.routes import utils

router = APIRouter()

router.include_router(utils.router)
