from flasgger import swag_from
from flask import Blueprint, Response, request
from flask_restful import Api

from app.docs.sample import *
from app.views import BaseResource

from app.models import db
from app.models.model import UserModel, RhythmWay


api = Api(Blueprint('sample_module', __name__))
api.prefix = '/sample'


@api.resource('')
class Sample(BaseResource):
    @swag_from(SAMPLE_GET)
    def get(self):
        return Response('', 200)

    def post(self):
        id = request.form['id']
        password = request.form['password']
        menstruation_period = request.form['mp']

        row = UserModel(id=str(id), password=str(password), menstruation_period=int(menstruation_period),
                        is_rhythm_contraception=True,
                        is_standard_contraception=False)
        db.session.add(row)
        db.session.commit()

        return Response('oh holy', 201)


@api.resource('/check')
class SampleCheck(BaseResource):
    def post(self):
        user_id = request.form['userId']

        row = RhythmWay(user_id=user_id, shortest_period=22, longest_period=30, recently_started_year=2018,
                        recently_started_month=7, recently_started_day=4)

        db.session.add(row)
        db.session.commit()

        return Response('success~~~~!!! ang gimothi', 201)
