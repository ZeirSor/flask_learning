from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__) # parameter template_folder=templates

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
        # return redirect('/index')
        return "login successfully"

    error = 'wrongUserNameOrPassword'
    return render_template("login.html", error=error)
    # return 'login failed'

@app.route('/index')
def index():
    return "FrontPage"

if __name__ == '__main__':
    app.run()

