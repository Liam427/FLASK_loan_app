from flask import Blueprint, render_template, request, url_for, session, redirect
from loan_app.models import Loan, Evaluation, db


mainbp = Blueprint('main', __name__)




@mainbp.route('/', methods=['GET', 'POST'])
def index():
    loan_list = Loan.query.all()
    if request.method == 'POST':
        get_form = request.form
        for i in range(1,215):
            if get_form[str(i)] != 'False':
                # eval_list = Evaluation.query.all()
                loan_score = Loan.query.filter(Loan.loan_id==i).first()
                loan_score.score = int(get_form[str(i)])
                db.session.add(loan_score)
                db.session.add(Evaluation(loan_id=i, score=get_form[str(i)]))
                db.session.commit()
            

        return redirect(url_for('main.index'))
    else:
        return render_template('index.html', loan_list=loan_list)


@mainbp.route('/selected', methods=['GET', 'POST'])
def selected():
    eval_selected = []
    loan_selected = []
    eval_list = Evaluation.query.all()
    for eval in eval_list:
        if eval.score != 'False' or False:
            eval_selected.append(eval)
            loan_selected.append(Loan.query.filter(Loan.loan_id == eval.loan_id).first())

    return render_template('selected.html', loan_selected=loan_selected)


# @mainbp.route('/predict', methods=['GET', 'POST'])
# def predict():