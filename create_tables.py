from config import Config
from main import create_app
from setup_db import db

if __name__ == '__main__':
    with create_app(Config).app_context():
        db.create_all()
