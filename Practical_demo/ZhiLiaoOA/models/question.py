from datetime import datetime

from exts import db
from models import User


class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(User, backref="questions")
