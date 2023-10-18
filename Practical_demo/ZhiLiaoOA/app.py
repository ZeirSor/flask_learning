
from flask import Flask, session, g, request, current_app
from flask_migrate import Migrate

from exts import init_exts, db, cache
from models import User

from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp


app = Flask(__name__)
app.config.from_object('config.settings')

# This sentence should be placed after app.config
init_exts(app)

migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


# before_request/ before_first_request/ after_request
# hook
@app.before_request
def my_before_request():
    # print('before request')
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)




@app.context_processor
def my_context_processor():
    # print('before request')
    return {'user': g.user}


@app.before_request
def before():
    print('route:       ', request.path)
    print('method:      ', request.method)
    print('client ip:   ', request.remote_addr)  # 客户端ip
    # print('client username:\t', type(request.remote_user))

    # 简单的反爬
    print(request.user_agent)   # python-requests/2.31.0
    if 'python' in request.user_agent.string:
        return 'You are using python crawler, bye!'
    #
    # 针对IP作反爬
    # ip = request.remote_addr
    # if cache.get(ip):
    #     # 做了拦截，不会进入视图函数
    #     return 'Boy, stop crawling!'
    # else:
    #     # 对每个ip设置缓存，一秒内不让重复访问
    #     cache.set(ip, 'value', timeout=1)

    g.idol = 'G.E.M.'
    print(g.idol)

    print(current_app)
    print(current_app.config)



if __name__ == '__main__':
    app.run()
