from flask_restful import Resource, fields, marshal_with, reqparse
from flask import jsonify
from models import User


# flask-restful Resource
# 使用类视图 CBV class based view
# 视图函数 FBV function based view

class HelloResource(Resource):
    def get(self):
        return jsonify({'msg': 'get request'})

    def post(self):
        return jsonify({'msg': 'post request'})

    def put(self):
        return jsonify({'msg': 'put request'})

    def delete(self):
        return jsonify({'msg': 'delete request'})


# flask-restful
# 字段格式化： 定义返回前端的数据格式

ret_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    # 'data': fields.String
    'like': fields.String(default='ball'),
    'like2': fields.String(),
    'data2': fields.String(attribute='data')
}


class UserResource(Resource):
    @marshal_with(ret_fields)
    def get(self):
        return {
            'status': 1,
            'msg': 'ok',
            'data': 'python'
        }


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'url': fields.Url('id', absolute=True)
}
ret_fields2 = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(user_fields)
}


class UserResource2(Resource):
    @marshal_with(ret_fields2)
    def get(self):
        user = User.query.first()
        return {
            'status': 1,
            'msg': 'ok',
            'data': user
        }


user_fields2 = {
    'username': fields.String,
    'password': fields.String,
}

ret_fields3 = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(user_fields2))
}


class UserResource3(Resource):
    @marshal_with(ret_fields3)
    def get(self):
        users = User.query.all()
        return {
            'status': 1,
            'msg': 'ok',
            'data': users
        }


# ---------------------------- 参数解析 ----------------------------
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='name is required parameter!')  # 必须参数
parser.add_argument('age', type=int, action='append')  # 可以有多个age
parser.add_argument('key', type=str, location='cookies')  # 获取cookies中的数据


class UserResource4(Resource):
    def get(self):
        args = parser.parse_args()
        name = args.get('name')
        age = args.get('age')
        key = args.get('key')

        return jsonify({'name': name, 'age': age, 'key': key})
