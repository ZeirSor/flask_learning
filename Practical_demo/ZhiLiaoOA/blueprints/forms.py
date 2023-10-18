import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired

from models import User, EmailCaptcha
from exts import db

class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="email format error!!!")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="captcha format error!!!")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="username format error!!!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="password format error!!!")])
    password_confirm = wtforms.StringField(validators=[EqualTo('password')])

    # 自定义验证：
    # 1.邮箱是否已经被注册
    # 2.验证码是否正确
    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError("email has been registered")

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        email_captcha = EmailCaptcha.query.filter_by(email=email, captcha=captcha).first()
        if not email_captcha:
            raise wtforms.ValidationError("captcha or email is error!!!")
        else:
            # todo: delete the captcha in the database which just be send
            db.session.delete(email_captcha)
            db.session.commit()


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="email format error!!!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="password format error!!!")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=2, max=100, message="title format error!!!")])
    content = wtforms.TextAreaField(validators=[Length(min=3, message="content format error!!!")])


class AnswerForm(wtforms.Form):
    content = wtforms.TextAreaField(validators=[Length(min=3, message="content format error!!!")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="question_id is required!!!")])
