from decouple import Config
from flask import Flask
from flask_restful import Api
from healthcheck import HealthCheck

from src.resources.users import Users

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://rafael_rotiroti:123456@127.0.0.1:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

health = HealthCheck(app, '/v1/health')
api.add_resource(Users, '/users', '/users/<int:user_id>')


if __name__ == '__main__':
    app.run(debug=Config('DEBUG'))
