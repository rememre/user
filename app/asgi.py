from time import perf_counter
from typing import Annotated, Callable

from fastapi import Depends, FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from .config.base import Base
from .config.logger import log_request, logger
from .config.postgres import Postgres
from .dependencies import get_db
from .routers import router

logger.info(f'Environment: {Base.name.title()} [{Base.env.upper()}]')
logger.info(f'PostgreSQL : {Postgres().url}')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = Base.origins,
    allow_credentials = True,
    allow_headers = ["*"],
    allow_methods = ["GET","POST","PUT"]
)

@app.middleware("http")
async def request_logger(request: Request, callback: Callable):
    start = perf_counter()
    response = await callback(request)
    processing_time = perf_counter() - start
    await log_request(request, response.status_code, processing_time)
    return response


@app.get('/healthcheck', status_code=status.HTTP_200_OK)
def healthcheck(db: Annotated[Session, Depends(get_db)]):
    status = "unhealthy"
    db_status = False
    try:
        db.execute(text("SELECT 1"))
        db_status = True
        status = "healthy"
    except Exception as e:
        print(repr(e))
    return {'status':status,'db': db_status}

app.include_router(router)
