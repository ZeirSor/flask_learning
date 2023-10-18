from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, Column, Integer, String

app = Flask(__name__)

app.config.from_object('config.settings')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

#
# `Flask-Migrate` 是一个 Flask 扩展，用于管理数据库迁移（migration）。数据库迁移是在应用程序已经部署并运行的情况下，对数据库结构进行更改或升级的过程。`Flask-Migrate` 与 SQLAlchemy 结合使用，可以轻松管理数据库模型的变更，同时保持数据的完整性。
#
# 以下是使用 `Flask-Migrate` 的一般步骤：
#
# 1. **安装 Flask-Migrate：** 如果你还没有安装 `Flask-Migrate`，可以使用 pip 安装它。
#
#    ```bash
#    pip install Flask-Migrate
#    ```
#
# 2. **初始化迁移环境：** 在你的 Flask 应用目录下，使用以下命令初始化数据库迁移环境。
#
#    ```bash
#    flask db init
#    ```
#
#    这个命令会创建一个名为 `migrations` 的目录，用于存储数据库迁移脚本。
#
# 3. **创建迁移脚本：** 当你更改了数据库模型（例如，添加、修改或删除表、列等），你需要创建一个迁移脚本以记录这些变更。
#
#    ```bash
#    flask db migrate -m "Description of the migration"
#    ```
#
#    这个命令将生成一个新的迁移脚本文件，其中包含了你的数据库模型变更的描述。你可以在生成的脚本文件中查看和确认数据库变更。
#
# 4. **应用迁移：** 使用以下命令将数据库模型的变更应用到数据库。
#
#    ```bash
#    flask db upgrade
#    ```
#
#    这个命令会将数据库模型的变更同步到实际的数据库中。
#
# 5. **回滚迁移：** 如果需要回滚到以前的版本，可以使用以下命令。
#
#    ```bash
#    flask db downgrade
#    ```
#
#    这个命令会将数据库回滚到之前的版本。
#
# 6. **查看迁移历史：** 你可以使用以下命令查看已经应用的迁移历史。
#
#    ```bash
#    flask db history
#    ```
#
# 7. **其他命令：** `Flask-Migrate` 还提供其他命令，如 `revision`（创建一个新的迁移脚本）、`show`（显示迁移状态）、`merge`（合并多个迁移脚本）等。
#
# 这些是基本的 `Flask-Migrate` 命令和用法。通过创建、应用和管理迁移脚本，你可以轻松地保持你的数据库模型与应用程序的需求同步，同时避免了手动维护数据库结构的繁琐工作。

# with app.app_context():
#     with db.session() as conn:
#         rs = conn.execute(text('select 1'))
#         print(rs.fetchall())


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    new_numeric_field = Column(Integer, nullable=False)

# with app.app_context():
#     db.create_all()

@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/user/add')
def add_user():
    user = User(username='zs', password='527')
    db.session.add(user)
    db.session.commit()
    return 'user create successfully'


@app.route('/user/query')
def query_user():
    # user = User.query.get(1)
    # print(f'{user.id}, {user.username}, {user.password}')

    users = User.query.filter_by(username='zs')
    print(type(users))
    for user in users:
        print(f'{user.id}, {user.username}, {user.password}')


    return "query successfully"

@app.route('/user/update')
def update_user():

    user = User.query.first()
    user.password = '725'
    db.session.commit()
    print(f'{user.id}, {user.username}, {user.password}')

    return 'update!'


@app.route('/user/delete')
def delete_user():

    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()

    print(f'{user.id}, {user.username}, {user.password}')

    return 'delete'

if __name__ == '__main__':
    app.run()


