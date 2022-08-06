from unittest.mock import MagicMock

import pytest

from app.dao.director import DirectorDAO
from app.dao.model.director import Director
from app.service.director import DirectorService


@pytest.fixture()
def dao_director():
    dao_director = DirectorDAO(None)

    yarik = Director(id=1, name="Yarik")
    jorik = Director(id=2, name="Jorik")
    kostik = Director(id=3, name="Kostik")

    dao_director.get_one = MagicMock(return_value=yarik)
    dao_director.get_all = MagicMock(return_value=[yarik, jorik, kostik])
    dao_director.create = MagicMock(return_value=Director(id=3))
    dao_director.delete = MagicMock()
    dao_director.update = MagicMock()

    return dao_director


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, dao_director):
        self.director_service = DirectorService(dao_director)

    def test_gen_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0
        assert type(directors) is list

    def test_create(self):
        data = {
            "name": "Egorka"
        }

        new_director = self.director_service.create(data)

        assert new_director is not None
        assert new_director.id is not None

    def test_update(self):
        data = {
            "id": 1,
            "name": "Vitaly"
        }

        self.director_service.update(data)

    def test_delete(self):
        self.director_service.delete(1)
