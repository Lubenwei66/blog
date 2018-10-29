#对整个应用的初始化操作
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
db=SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@localhost:3306/blog'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['SECRET_KEY']='ye ye zai ci'#session密匙
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)
    return app


