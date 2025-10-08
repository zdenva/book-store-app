from fastapi import APIRouter

from bookstore.api.routes import utils

router = APIRouter()

router.include_router(utils.router)
