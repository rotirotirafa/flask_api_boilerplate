from typing import Dict

from flask_restful import Resource
from flask import jsonify, request

from sqlalchemy.exc import IntegrityError

from app.services.trips import TripsService


class Matches(Resource):
    service = TripsService()

    def get(self, match_id=None) -> Dict:
        if match_id:
            match = self.service.get_one(match_id)
            return {'match': match}
        matches = self.service.get_all()
        return {'matches': matches}

    def put(self, match_id) -> Dict:
        payload = request.get_json()
        return self.service.update(payload, match_id)

    def post(self):
        try:
            payload = request.get_json()
            return self.service.create(payload)
        except IntegrityError as ex:
            return {"message": "Email exists, sign in."}, 406
        except Exception as ex:
            print(ex)

    def delete(self, trip_id) -> Dict:
        return {'Deleted': trip_id}
