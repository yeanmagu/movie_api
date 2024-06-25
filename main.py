from fastapi import FastAPI

from api.router.movie import movie_router
from api.router.user import user_router
from infraestructure.config.database import engine, Base
from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "2"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


