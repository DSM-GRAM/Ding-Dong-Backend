import os

from app import create_app
from app.models import db

from config.dev import DevConfig
from config.production import ProductionConfig


if __name__ == '__main__':
    app = create_app(DevConfig)
    db.create_all(app=app)

    if 'SECRET_KEY' not in os.environ:
        print('[WARN] SECRET KEY is not set in the environment variable.')

    app.run(**app.config['RUN_SETTING'])
