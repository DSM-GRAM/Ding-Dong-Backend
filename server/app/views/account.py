from flasgger import swag_from
from flask import Blueprint, Response, request
from flask_restful import Api
from werkzeug.security import generate_password_hash, check_password_hash

from app.docs.signup import *
from app.views import BaseResource, json_required

from app.models import db
from app.models.model import UserModel

api = Api(Blueprint(__name__, __name__))


@api.resource('/signup')
class SignUp(BaseResource):
    @swag_from(SIGNUP_POST)
    @json_required({'id': str, 'password': str, 'period': int})
    def post(self):
        """
        회원가입
        """
        id = request.json['id']
        password = request.json['password']
        menstruation_period = request.json['period']

        hashed_pw = generate_password_hash(password)

        if UserModel.query.filter_by(id=id):
            return Response('ID duplicated', 409)

        query = {
            'id': id,
            'password': hashed_pw,
            'menstruation_period': menstruation_period
        }

        if (menstruation_period >= 26) and (menstruation_period <= 32):
            query.update({
                'is_rhythm_contraception': False,
                'is_standard_contraception': True
            })

        else:
            query.update({
                'is_rhythm_contraception': True,
                'is_standard_contraception': False
            })

        db.session.add(**query)
        db.session.commit()

        return Response('', 201)


@api.resource('/login')
class SignIn(BaseResource):
    def post(self):
        """
        로그인
        """
        pass

