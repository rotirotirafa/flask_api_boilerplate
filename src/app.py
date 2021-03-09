from decouple import Config
from flask import Flask
# from flask_restful import Api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://rafael_rotiroti:123456@127.0.0.1:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# from src.models.user import User

# api = Api(app)
#
# api.add_resource(users, '/users')

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=Config('DEBUG'))
