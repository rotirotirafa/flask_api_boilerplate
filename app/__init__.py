from flask import Flask
from app.ext import db, migrate
from flask_restful import Api

from app.models import tables


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")
    api = Api(app)
    # Extensions
    db.configure(app)
    migrate.configure(app)

    from app.resources.users import Users
    api.add_resource(Users, '/users', '/users/<int:user_id>')

    return app
