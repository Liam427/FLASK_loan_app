from flask import Blueprint, render_template, request, url_for, session, redirect
from loan_app.models import Loan, Evaluation


mainbp = Blueprint('main', __name__)




@mainbp.route('/')
def index():
    loan_list = Loan.query.all()
    return render_template('index.html', loan_list=loan_list)
