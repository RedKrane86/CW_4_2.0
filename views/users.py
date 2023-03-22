from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service


user_ns = Namespace('user')


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UserSchema().dump(user)
        return result, 200

    def patch(self, uid):
        req_json = request.json
        if 'id' not in req_json:
            req_json['id'] = uid
        user_service.update(req_json)
        return '', 204


@user_ns.route('/password')
class UserView(Resource):
    def put(self, password_hash, other_password):
        user_service.compare_passwords(password_hash, other_password)
        return '', 204
