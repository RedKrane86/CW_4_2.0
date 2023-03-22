from marshmallow import Schema, fields

from setup_db import db
from .base import Base


class Genre(Base):
    __tablename__ = 'genre'
    name = db.Column(db.String(255), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
