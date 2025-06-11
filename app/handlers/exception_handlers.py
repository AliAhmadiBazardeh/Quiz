import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger("app_error_logger")
logging.basicConfig(level=logging.INFO)

async def global_exception_handler(request: Request, exc: Exception):

    logger.error(f"Unhandled error at {request.url.path}: {exc}", exc_info=True)

    if isinstance(exc, StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )
    
    if isinstance(exc, RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors()}
        )
 
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error."}
    )