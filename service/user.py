import hashlib
import base64
import hmac

from constrains import PWD_HASH_ITERATIONS, PWD_HASH_SALT
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, user_data):
        user_data['password'] = self.get_hash(user_data.get('password'))
        return self.dao.create(user_data)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    def get_hash(self, password):
        return base64.b64encode(
            hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            )
        )

    def compare_passwords(self, password_hash, other_password):
        return hmac.compare_digest(
            password_hash,
            self.get_hash(other_password),
        )
