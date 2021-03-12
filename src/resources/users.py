from typing import Dict

from flask_restful import Resource
from flask import jsonify, request


class Users(Resource):

    def get(self) -> Dict:
        users = [
            {
                "user_id": 1,
                "name": "rafael",
                "age": 25
            },
            {
                "user_id": 2,
                "name": "ana",
                "age": 24
            }
        ]
        return {'users': users}

    def put(self, user_id) -> Dict:
        return {'Update': user_id}

    def post(self) -> Dict:
        return jsonify(request.get_json())

    def delete(self, user_id) -> Dict:
        return {'Deleted': user_id}
