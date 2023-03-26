from contextlib import suppress
from typing import Any, Dict, List, Type

from sqlalchemy.exc import IntegrityError

from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from main import create_app
from setup_db import db
from utils import read_json


def load_data(data: List[Dict[str, Any]], model) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))



if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(Config)

    with app.app_context():
        load_data(fixtures['genres'], Genre)
        load_data(fixtures['directors'], Director)
        load_data(fixtures['movies'], Movie)

        with suppress(IntegrityError):
            db.session.commit()
