import random
import string
import time

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from exts import mail, db, cache
from models import EmailCaptcha, User
from .forms import RegisterForm, LoginForm

bp = Blueprint("auth", __name__, url_prefix='/auth')

@bp.route('/index')
@cache.cached(timeout=20)   # 给视图函数加入一个缓存20s, 20s内第二次访问这个视图函数直接从缓存中取
def index():
    print('Index')

    time.sleep(5)
    return render_template('index.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if not user:
                print('The mailbox does not exist in the database！')
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                # login status
                # cookie: 不适合存储太多数据，只适合存储少量数据
                #         一般用来存放登录授权的东西
                # session: flask 中的session是经过加密后存储在cookie中的
                session['user_id'] = user.id
                return redirect('/')
            else:
                print('The password is incorrect！')

        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


# GET   get data from server
# POST  commit the data to server
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # flask-wtf: wtforms
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = User(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))



@bp.route("/logout")
def logout():
    session.clear()
    return redirect('/')


@bp.route('/captcha/email')
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get('email')

    # 4/6 随机数组、数字、数组、字母的组合
    source = string.digits * 4
    captcha = "".join(random.sample(source, 4))

    # send message
    message = Message(subject="captcha test", recipients=[email], body="your captcha is: {}".format(captcha))
    mail.send(message)

    # 存储邮箱验证码
    # memcached/redis
    # use database table to storage
    email_captcha = EmailCaptcha(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()

    # print(captcha)
    # RESTful APT
    return jsonify({"code": 200, "message": "", "data": None})



@bp.route('/captcha/phone')
def get_phone_captcha():
    pass



@bp.route('/mail/test')
def mail_test():
    message = Message(subject="Test", recipients=["1418681525@qq.com"], body="Test")
    mail.send(message)
    return "email send successful!"