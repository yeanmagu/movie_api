from __future__ import annotations

from abc import ABC

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse


class ErrorHandler(BaseHTTPMiddleware, ABC):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as ex:
            return JSONResponse(status_code=500, content={"error": str(ex)})
