from flasgger import swag_from
from flask import Blueprint, Response
from flask_restful import Api, request

from app.docs.signup import *
from app.views import BaseResource, json_required

from app.models import db
from app.models.model import UserModel

api = Api(Blueprint(__name__, __name__))


@api.resource('/signup')
class SignUp(BaseResource):
    @swag_from(SIGNUP_POST)
    @json_required({'id': str, 'password': str})
    def post(self):
        """
        회원가입
        """
        id = request.json['id']
        password = request.json['password']
