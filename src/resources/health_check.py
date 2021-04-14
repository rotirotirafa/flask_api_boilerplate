from flask_restful import Resource


class HealthCheck(Resource):

    @classmethod
    def get(cls):
        return 'im Alive', 200
