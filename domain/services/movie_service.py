from infraestructure.config.database import Session
from infraestructure.entities.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService:

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_movies(self):
        movies = self.db.query(MovieModel).all()
        return movies

    def get_movie(self, id: int):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return movie

    def get_movie_by_category(self, category: str):
        movie = self.db.query(MovieModel).filter(MovieModel.category == category).first()
        return movie

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return

    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.category = data.category
        movie.year = data.year
        self.db.commit()
        return

    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
