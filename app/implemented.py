from app.dao.movie import MovieDAO
from app.dao.director import DirectorDAO
from app.dao import GenreDAO
from app.service.movie import MovieService
from app.service.genre import GenreService
from app.service import DirectorService
from setup_db import db

movie_dao = MovieDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)

movie_service = MovieService(dao=movie_dao)
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)