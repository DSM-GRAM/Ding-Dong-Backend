from datetime import timedelta
import os


class Config:
    SERVICE_NAME = 'Ding-Dong'
    SERVICE_NAME_UPPER = SERVICE_NAME.upper()
    DOMAIN = None

    RUN_SETTING = {
        'threaded': True
    }

    SECRET_KEY = os.getenv('SECRET_KEY', '85c145a16bd6f6e1f3e104ca78c6a102')

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=300)
    JWT_HEADER_TYPE = 'JWT'

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:germany33@localhost:3306/soccer"

    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': os.getenv('SWAGGER_URI', '/docs'),
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/ '
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Some Tag',
                'description': 'Some API'
            },
            {
                'name': '계정',
                'description': '계정과 관련된 API'
            }
        ]
    }
