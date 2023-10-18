# 路由文件 urls.py

from exts import api
from apis import *

api.add_resource(HelloResource, '/hello', endpoint='id')
api.add_resource(UserResource, '/user')
api.add_resource(UserResource2, '/user2')
api.add_resource(UserResource3, '/user3')
api.add_resource(UserResource4, '/user4')
