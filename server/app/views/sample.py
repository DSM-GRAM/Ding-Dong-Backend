from flasgger import swag_from
from flask import Blueprint, Response, request
from flask_restful import Api

from app.docs.sample import *
from app.views import BaseResource

from app.models import db
from app.models.sample import SoccerModel

api = Api(Blueprint('sample_module', __name__))
api.prefix = '/sample'


@api.resource('/')
class Sample(BaseResource):
    @swag_from(SAMPLE_GET)
    def get(self):
        return Response('', 200)


@api.resource('/add')
class AccountPlayer(BaseResource):
    def post(self):
        player = request.form['player']
        back_number = request.form['backNumber']

        row = SoccerModel(player=player, back_number=back_number)
        db.session.add(row)
        db.session.commit()

        return Response('Oh My God. Lucky~!!!', 201)
