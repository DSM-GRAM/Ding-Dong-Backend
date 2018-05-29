from app.models import db
from sqlalchemy import VARCHAR


class UserModel(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    menstruation_period = db.Column(db.Integer, nullable=False)
    is_rhythm_contraception = db.Column(db.Boolean, nullable=False)
    is_standard_contraception = db.Column(db.Boolean, nullable=False)
    push_notification = db.Colimn(db.Boolean, default=True)


class RhythmWay(db.Model):
    __tablename__ = 'rhythm_constraception'

    user_id = db.Column(db.String(100), primary_key=True)
    shortest_period = db.Column(db.Integer, nullable=False)
    longest_period = db.Column(db.Integer, nullable=False)
    recently_started_year = db.Column(db.Integer, nullable=False)
    recently_started_month = db.Column(db.Integer, nullable=False)
    recently_started_day = db.Column(db.Integer, nullable=False)
