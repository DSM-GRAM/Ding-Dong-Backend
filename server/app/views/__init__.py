from functools import wraps
import ujson

from flask import Response, abort, g, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


def after_request(response):
    """
    보안 헤더 설정
    """
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'deny'

    return response


def auth_required(model):
    def decorator(fn):
        """
        View decorator for access control
        """
        @wraps(fn)
        @jwt_required
        def wrapper(*args, **kwargs):
            user = model.objects(id=get_jwt_identity()).first()
            if not user:
                abort(403)

            g.user = user

            return fn(*args, **kwargs)
        return wrapper
    return decorator


def json_required(required_keys):
    """
    View decorator for JSON validation.

    - If content-type is not application/json : returns status code 406
    - If required_keys are not exist on request.json : returns status code 400

    Args:
        required_keys (dict): Required keys on requested JSON payload
    """
    def decorator(fn):
        if fn.__name__ == 'get':
            print('[WARN] JSON with GET method? on "{}()"'.format(fn.__qualname__))

        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(406)

            for key, typ in required_keys.items():
                if key not in request.json or not type(request.json[key]) is typ:
                    abort(400)
                if typ is str and not request.json[key]:
                    abort(400)

            return fn(*args, **kwargs)
        return wrapper
    return decorator


class BaseResource(Resource):
    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200, **kwargs) -> Response:
        """
        Helper function which processes json response with unicode using ujson

        Args:
            data (dict and list): Data for dump to JSON
            status_code (int): Status code for response
        """
        return Response(
            ujson.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8',
            **kwargs
        )


class Router:
    """
    REST resource routing helper class like standard flask 3-rd party libraries
    """
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Routes resources. Use app.register_blueprint() aggressively
        """
        app.after_request(after_request)

        from app.views import sample
        app.register_blueprint(sample.api.blueprint)
