from flask import Flask
from applications.admin import init_blue_admin
from applications.config import Config
from extensions.sql import init_db
def create_app():
    app = Flask(__name__,static_folder='static',template_folder='templates')
    app.config.from_object(Config)
    init_db(app)#将app以懒加载传给模型
    init_blue_admin(app)
    return app