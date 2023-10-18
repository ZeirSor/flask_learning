from flask import Blueprint, request, jsonify

bp = Blueprint("auth", __name__, url_prefix='/auth')


@bp.route('/')
def index():
    return 'index'


@bp.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'GET':
        return jsonify({'method': 'GET'})
    elif request.method == 'POST':
        return jsonify({'method': 'POST'})
    elif request.method == 'PUT':
        return jsonify({'method': 'PUT'})
    elif request.method == 'DELETE':
        return jsonify({'method': 'DELETE'})
