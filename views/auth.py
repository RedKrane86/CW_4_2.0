from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service
from implemented import user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')

        if not all([email, password]):
            return '', 400

        new_user = user_service.create(req_json)

        return '', 201


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json['email']
        password = req_json['password']

        if not all([email, password]):
            return '', 400

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        req_json = request.json
        token = req_json.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
