from flask import Flask

from src.settings import HOST, PORT


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return True

    # build url
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
