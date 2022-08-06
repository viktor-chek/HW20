from unittest.mock import MagicMock

import pytest

from app.dao.model.movie import Movie
from app.service.movie import MovieService
from app.dao.movie import MovieDAO


@pytest.fixture()
def dao_movie():
    dao_movie = MovieDAO(None)

    movie1 = Movie(id=1, title="Зеленая миля", description="Пол Эджкомб не верил в чудеса. Пока не столкнулся с одним из них", trailer="ссылка на трейлер", year=1999, rating=1)
    movie2 = Movie(id=2, title="Форрест Гамп", description="Мир уже никогда не будет прежним, после того как вы увидите его глазами Форреста Гампа", trailer="ссылка на трейлер", year=1994, rating=4)
    movie3 = Movie(id=3, title="Побег из Шоушенка",description="Страх - это кандалы. Надежда - это свобода", trailer="ссылка на трейлер", year=1994, rating=3)

    dao_movie.get_one = MagicMock(return_value=movie1)
    dao_movie.get_all = MagicMock(return_value=[movie2, movie1, movie3])
    dao_movie.create = MagicMock(return_value=Movie(id=3))
    dao_movie.delete = MagicMock()
    dao_movie.update = MagicMock()

    return dao_movie


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, dao_movie):
        self.movie_service = MovieService(dao_movie)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None
        assert movie.title is not None
        assert movie.description is not None
        assert type(movie.year) is int
        assert type(movie.rating) is int

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert type(movies) is list

    def test_create(self):
        data = {
            "title": "Темный рыцарь",
            "description": "Добро пожаловать в мир Хаоса!",
            "trailer": "ссылка на трейлер",
            "year": 2008,
            "rating": 15
        }

        new_movie = self.movie_service.create(data)
        assert new_movie is not None
        assert new_movie.id is not None

    def test_update(self):
        data = {
            "id": 1,
            "title": "Обновил название фильма",
            "description": "обновил описание фильма",
            "trailer": "новая ссылка на трейлер",
            "year": 2015,
            "rating": 31
        }

        self.movie_service.update(data)

    def test_delete(self):
        self.movie_service.delete(1)
