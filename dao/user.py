from sqlalchemy.exc import IntegrityError

from exception import UserAlreadyExists
from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_data):
        try:
            result = User(**user_data)
            self.session.add(result)
            self.session.commit()
        except IntegrityError:
            raise UserAlreadyExists
        return result

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_data):
        user = self.get_one(user_data.get("id"))
        if user_data.get("email"):
            user.email = user_data.get("email")
        if user_data.get("password"):
            user.password = user_data.get("password")
        if user_data.get("name"):
            user.name = user_data.get("name")
        if user_data.get("surname"):
            user.surname = user_data.get("surname")
        if user_data.get("favorite_genre"):
            user.favorite_genre = user_data.get("favorite_genre")

        try:
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            raise UserAlreadyExists
