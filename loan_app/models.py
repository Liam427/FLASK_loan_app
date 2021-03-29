from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


class Loan(db.Model):
    __tablename__ = 'loan'

    loan_id = db.Column(db.Integer(), nullable=False, primary_key=True)
    bank_name = db.Column(db.String(), nullable=False)
    loan_name = db.Column(db.String(), nullable=False)
    rpay = db.Column(db.String(), nullable=False)
    rate_type = db.Column(db.String(), nullable=False)
    rate_min = db.Column(db.Float())
    rate_max = db.Column(db.Float())
    rate_avg = db.Column(db.Float())
    score = db.Column(db.Integer())

    def __repr__(self):
        return f"Loan {self.loan_id}"


# 유저가 선택해서 post하면 db에 넣기
class Evaluation(db.Model):
    __tablename__ = 'evaluation'

    id = db.Column(db.Integer(), primary_key=True)
    loan_id = db.Column(db.String(), db.ForeignKey('loan.loan_id'), nullable=False)
    score = db.Column(db.Integer(), nullable=False)


    def __repr__(self):
        return f'<Evaluation {self.id} {self.loan_id} {self.score}>'