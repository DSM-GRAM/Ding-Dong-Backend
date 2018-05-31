from app.models import db


class UserModel(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    menstruation_period = db.Column(db.Integer, nullable=False)
    is_rhythm_contraception = db.Column(db.Boolean, nullable=False)
    is_standard_contraception = db.Column(db.Boolean, nullable=False)
    push_notification = db.Column(db.Boolean, default=True)


class RhythmWay(db.Model):
    __tablename__ = 'rhythm_constraception'

    user_id = db.Column(db.String(100), db.ForeignKey('User.id'), primary_key=True)
    shortest_period = db.Column(db.Integer, nullable=False)
    longest_period = db.Column(db.Integer, nullable=False)
    recently_started_year = db.Column(db.Integer, nullable=False)
    recently_started_month = db.Column(db.Integer, nullable=False)
    recently_started_day = db.Column(db.Integer, nullable=False)


class StandardWay(db.Model):
    __tablename__ = 'standard_constraception'

    user_id = db.Column(db.String(100), db.ForeignKey('User.id'), primary_key=True)
    menstruation_month = db.Column(db.Integer, primary_key=True)


class MenstruationPeriod(db.Model):
    __tablename__ = 'menstruation_period'

    user_id = db.Column(db.String(100), db.ForeignKey('standard_constraception.user_id'), primary_key=True)
    menstruation_month = db.Column(db.Integer, db.ForeignKey('standard_constraception.menstruation_month'), primary_key=True)
    first_menstruation_date = db.Column(db.Integer, nullable=False)
    last_menstruation_date = db.Column(db.Integer, nullable=False)


class BeforeMenstruationSymptom(db.Model):
    __tablename__ = 'before_menstruation_symptom'

    user_id = db.Column(db.String(100), db.ForeignKey('User.id'), primary_key=True)
    symptom_category = db.Column(db.Integer, primary_key=True)


class SymptomData(db.Model):
    __tablename__ = 'symptom_data'

    user_id = db.Column(db.String(100), db.ForeignKey('before_menstruation_symptom.user_id'), primary_key=True)
    symptom_category = db.Column(db.Integer, db.ForeignKey('before_menstruation_symptom.symptom_category'), primary_key=True)
    cate1 = db.Column(db.Boolean, default=False)
    cate2 = db.Column(db.Boolean, default=False)
    cate3 = db.Column(db.Boolean, default=False)
    cate4 = db.Column(db.Boolean, default=False)
    cate5 = db.Column(db.Boolean, default=False)
