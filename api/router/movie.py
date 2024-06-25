from typing import List

from fastapi import Depends, Path, Query, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from infraestructure.config.database import Session
from infraestructure.entities.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from schemas.movie import Movie

from domain.services.movie_service import MovieService

movie_router = APIRouter()


@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> JSONResponse:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200, dependencies=[Depends(JWTBearer())])
def get_movie(id: int = Path(ge=1, le=2000)) -> JSONResponse:
    db = Session()
    movie = MovieService(db).get_movie(id)
    if not movie:
        return JSONResponse(status_code=404, content={"message": "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(movie))


@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movie_by_category(category: str = Query(min_length=5, max_length=15)) -> JSONResponse:
    db = Session()
    movies = MovieService(db).get_movie_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(movies))


@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> JSONResponse:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})


@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> JSONResponse:
    db = Session()
    movie_filter = MovieService(db).get_movie(id)

    if not movie_filter:
        return JSONResponse(status_code=404, content={"message": "Registro no encontrado"})

    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})


@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> JSONResponse:
    db = Session()
    movie_filter = MovieService(db).get_movie(id)

    if not movie_filter:
        return JSONResponse(status_code=404, content={"message": "Registro no encontrado"})

    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})
