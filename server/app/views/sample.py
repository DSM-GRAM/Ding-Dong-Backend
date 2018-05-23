from flasgger import swag_from
from flask import Blueprint, Response
from flask_restful import Api

from app.docs.sample import *
from app.views import BaseResource

api = Api(Blueprint('sample_module', __name__))
api.prefix = '/prefix'


@api.resource('/sample')
class Sample(BaseResource):
    @swag_from(SAMPLE_GET)
    def get(self):
        return Response('', 200)
