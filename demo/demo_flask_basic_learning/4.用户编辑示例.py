import functools

from flask import Flask, render_template, jsonify, request, redirect, url_for, session

app = Flask(__name__)  # parameter template_folder=templates

app.secret_key = "asff6ferwfwer5dfc3asdfsd0n890I0u8TV6s3dx"

DATA_DICT = {
    1: {
        "name": "Mike",
        "age": 18
    },
    2: {
        "name": "Sarah",
        "age": 25
    },
    3: {
        "name": "John",
        "age": 30
    }
}


def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        username = session.get('zs')
        if not username:
            return redirect(url_for('login'))
        return func(*args, **kwargs)

    return inner


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
        # return "login"
        # return render_template("login.html")
        # return jsonify({'code': 1000, 'data': [1, 2, 3]})

    # print(request.form.get)
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'zs' and pwd == 'zs':
        session['zs'] = 'zs'
        return redirect('/index')
        # return "login successfully"

    error = 'wrongUserNameOrPassword'
    return render_template("login.html", error=error)
    # return 'login failed'


@app.route('/index', endpoint='idx')
@auth
def index():
    data_dict = DATA_DICT
    return "FrontPage"
    # return render_template('index.html', data_dict=data_dict)


@app.route('/edit', methods=['GET', 'POST'])
@auth
def edit():
    nid = int(request.args.get('nid'))
    print(nid, type(nid))

    if request.method == 'GET':
        info = DATA_DICT[int(nid)]
        return render_template('edit.html', info=info)

    user = request.form.get('user')
    age = request.form.get('age')
    DATA_DICT[nid]['name'] = user
    DATA_DICT[nid]['age'] = age
    return redirect(url_for('idx'))


@app.route('/del/<int:nid>')
@auth
def delete(nid):
    # nid = request.args.get('nid')
    print(nid)
    del DATA_DICT[nid]
    return redirect(url_for('idx'))


if __name__ == '__main__':
    app.run()
