from flask import Blueprint, render_template, request, url_for, session, redirect
from loan_app.models import Loan, Evaluation, db


mainbp = Blueprint('main', __name__)




@mainbp.route('/', methods=['GET', 'POST'])
def index():
    loan_list = Loan.query.all()
    if request.method == 'POST':
        get_form = request.form
        for i in range(1,215):
            if get_form[str(i)]:
                loan_id = i
                eval_list = Evaluation.query.all()
                loan_score = Loan.query.filter(Loan.id==eval_list).first()
                loan_score.score = loan_score(get_form[str(i)])
                db.session.add(Evaluation(loan_id=i, score=get_form[str(i)]), loan_score)
                db.session.commit()

        return redirect(url_for('main.index'))
    else:
        return render_template('index.html', loan_list=loan_list)


@mainbp.route('/selected', methods=['GET', 'POST'])
def selected():
    eval_selected = []
    eval_list = Evaluation.query.all()
    for eval in eval_list:
        if eval.score:
            eval_selected.append(eval)
    return render_template(eval_selected=eval_selected)


# @mainbp.route('/predict', methods=['GET', 'POST'])
# def predict():