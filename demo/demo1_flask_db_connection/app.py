from flask import Flask, request, render_template, url_for, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

app.config.from_object('config.settings')

# 在app.config中设置好连接数据库的信息，
# 然后使用SQLAlchemy(app)创建一个db对象
# SQLAlchemy会自动读取app.config中连接数据库的信息
db = SQLAlchemy(app)

with app.app_context():
    with db.session() as conn:
        rs = conn.execute(text('select 1'))
        print(rs.fetchall())


class User():
    def __init__(self, username, email):
        self.username = username
        self.email = email


def datetime_format(value, format='%Y-%m-%d %H:%m:%S'):
    print(type(value))
    return value.strftime(format)


class Class(db.Model):
    __tablename__ = 'class'

    ClassID = db.Column(db.String(20), primary_key=True, nullable=False)
    ClassName = db.Column(db.String(20))

    def __init__(self, ClassID, ClassName):
        self.ClassID = ClassID
        self.ClassName = ClassName

    def __repr__(self):
        return f"<Class(ClassID='{self.ClassID}', ClassName='{self.ClassName}')>"


app.add_template_filter(datetime_format, 'd_format')


# 测试数据库连接的路由
@app.route('/test_db_connection', methods=['GET'])
def test_db_connection():
    try:
        # 尝试查询数据库
        class_ = Class.query.first()
        print(class_)
        if class_:
            return jsonify({'message': 'DATABASE_CONNECTION_SUCCESSFUL!'})
        else:
            return jsonify({'message': 'DATABASE_QUERY_IS_EMPTY!'})
    except Exception as e:
        return jsonify({'message': f'DATABASE_CONNECTION_FAILED：{str(e)}'})


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello world!'


@app.route('/profile')
def profile():
    return 'profile'


@app.route('/blog/list')
def blog_list():
    return 'blog list'


@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    # return f"visit blog id: {blog_id}"
    return render_template('blog_detail.html', blog_id=blog_id, username="zerisor")


@app.route('/book/list')
def book_list():
    page = request.args.get('page', default=1, type=int)
    return f'visit book list: {page}'


@app.route('/index')
def index():
    user = User(username='zeirsor', email='xx@gmail.com')
    person = {
        "username": "random_user123",
        "email": "random_user123@example.com"
    }
    return render_template('index.html', user=user, person=person)


@app.route('/filter')
def fileter_demo():
    user = User(username='zeirSor', email='xx@gmail.com')
    time = datetime.now()
    return render_template('filter.html', user=user, time=time)


@app.route('/control')
def control_statement():
    age = 17.9
    books = [
        {
            "bookname": "The Great Gatsby",
            "author": "F. Scott Fitzgerald"
        },
        {
            "bookname": "To Kill a Mockingbird",
            "author": "Harper Lee"
        },
    ]

    return render_template('control.html', age=age, books=books)


@app.route('/child1')
def child1():
    return render_template('child1.html')


@app.route('/child2')
def child2():
    return render_template('child2.html')


@app.route('/static')
def static_demo():
    return render_template('static.html')


if __name__ == '__main__':
    # app.debug = True
    app.run()
