from exts import db


class EmailCaptcha(db.Model):
    __tablename__ = 'email_captcha'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)

    used = db.Column(db.Boolean, default=False)