from flask import Blueprint

xwy = Blueprint('wy', __name__)


@xwy.route('/f1')
def f1():
    return 'xwyf1'


@xwy.route('/f2')
def f2():
    return 'xwyf2'
