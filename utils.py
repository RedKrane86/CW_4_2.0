import json
from typing import Union
import jwt
from flask import request
from flask_restx import abort

from constrains import JWT_SECRET, JWT_ALGORITHM


def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print('JWT Decode exception', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper
