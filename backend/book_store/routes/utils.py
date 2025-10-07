from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import text

from book_store.core.deps import SessionDep

router = APIRouter(prefix="/utils", tags=["utils"])


@router.get("/health-check/")
async def health_check() -> bool:
    return True


@router.get("/health-check/db")
async def health_check_db(session: SessionDep):
    try:
        session.exec(text("SELECT 1"))
        return True
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "fail", "db": str(e)})
