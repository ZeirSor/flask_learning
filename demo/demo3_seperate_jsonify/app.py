from flask import Flask

from exts import init_exts, db
from blueprints.auth import bp as auth_bp
from urls import *

app = Flask(__name__)
app.config.from_object('config.settings')

# This sentence should be placed after app.config
init_exts(app)

# app.register_blueprint(qa_bp)
# app.register_blueprint(auth_bp)

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
