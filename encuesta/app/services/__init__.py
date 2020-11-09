from flask import Blueprint
from flask_restful import Api, Resource
from . import dates

services = Blueprint('services', __name__)

api = Api(services)


class AgeResource(Resource):
    def get(self, birthDate):
        age = dates.calculateAge(birthDate)
        return {"years": age[0], "months": age[1], "days": age[2]}


api.add_resource(AgeResource, '/api/<birthDate>')
