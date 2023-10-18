from datetime import datetime

from exts import db
from models import Question
from models import User


class Answer(db.Model):
    __tablename__ = "answer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    question = db.relationship(Question, backref=db.backref("answers", order_by=create_time.desc()))
    author = db.relationship(User, backref="answers")