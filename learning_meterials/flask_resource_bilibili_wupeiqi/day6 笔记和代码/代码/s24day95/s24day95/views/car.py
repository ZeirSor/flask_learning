from flask import Blueprint,render_template

car = Blueprint('car',__name__)


@car.route('/index',strict_slashes=False)
def index():
    return render_template('car/index.html')


@car.route('/add')
def add():
    return render_template('car/add.html')