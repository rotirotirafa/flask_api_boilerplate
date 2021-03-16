from typing import Dict

from flask_restful import Resource
from flask import jsonify, request

from sqlalchemy.exc import IntegrityError

from app.services.matches import MatchesService


class Matches(Resource):
    service = MatchesService()

    def get(self) -> Dict:
        matches = self.service.get_all()
        return {'matches': matches}

    def post(self):
        try:
            payload = request.get_json()
            return self.service.create(payload)
        except IntegrityError as ex:
            return {"message": "Cant Match"}, 406
        except Exception as ex:
            print(ex)
