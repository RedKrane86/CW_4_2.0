from marshmallow import Schema, fields

from setup_db import db
from .base import Base


class Director(Base):
    __tablename__ = 'director'
    name = db.Column(db.String(255), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
