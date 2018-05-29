from sqlalchemy import Column, VARCHAR
from app.models import db


class SoccerModel(db.Model):
    __tablename__ = 'SoccerModel'

    player = Column(VARCHAR(100), primary_key=True)
    back_number = Column(VARCHAR(100), nullable=False)
