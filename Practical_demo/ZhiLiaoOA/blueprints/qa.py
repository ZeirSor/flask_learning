from flask import Blueprint, request, render_template, g, redirect, url_for

from .forms import QuestionForm, AnswerForm
from models import Question, Answer
from exts import db
from decorates import login_required

bp = Blueprint("qa", __name__, url_prefix='/')


@bp.route('/')
def index():
    print('g.idol:      ', g.idol)
    questions = Question.query.order_by(Question.create_time.desc()).all()
    return render_template("index.html", questions=questions)



@bp.route('/qa/public', methods=['GET', 'POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = Question(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            # todo: 跳转到问答的详情页
            return redirect('/')
        else:
            print(form.errors)
            return redirect(url_for("qa.public_question"))


@bp.route('/qa/detail/<question_id>')
def qa_detail(question_id):
    question = Question.query.get(question_id)
    return render_template("detail.html", question=question)


# @bp.route('/answer/public', methods=['GET', 'POST'])
@bp.post('/answer/public')
@login_required
def public_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = Answer(content=content, author_id=g.user.id, question_id=question_id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.qa_detail", question_id=question_id))  # 用form去取可能为空
    else:
        print(form.errors)
        return redirect(url_for("qa.qa_detail", question_id=request.form.get("question_id")))  # 用form去取可能为空


@bp.route('/search')
def search():
    # /search?q=flask
    # /search?<q>
    # post, request.form
    q = request.args.get('q')
    questions = Question.query.filter(Question.title.contains(q)).all()
    return render_template('index.html', questions=questions)