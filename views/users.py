import jwt
from flask import request
from flask_restx import Resource, Namespace

from constrains import JWT_SECRET, JWT_ALGORITHM
from dao.model.user import UserSchema
from implemented import user_service
from utils import auth_required

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        result = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = user_service.get_by_email(result['email'])
        result = UserSchema().dump(user)
        return result, 200

    @auth_required
    def patch(self):
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        result = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

        req_json = request.json
        if 'email' not in req_json:
            req_json['email'] = result['email']
        user_service.update(req_json)

        return '', 204


@user_ns.route('/password')
class UserView(Resource):
    @auth_required
    def put(self, password_hash, other_password):
        user_service.compare_passwords(password_hash, other_password)
        return '', 204
