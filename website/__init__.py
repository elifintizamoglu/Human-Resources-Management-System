from calendar import c
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager
from flask_session import Session
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()
def create_app():
    app = Flask(__name__)
    # encrypt or secure the cookies and session data related to our website
    app.config['SECRET_KEY'] = 'elif is here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:246135@localhost:5432/HRMS_DB'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    db.init_app(app)
    migrate = Migrate(app, db)
    cors.init_app(app)
    Session(app)
    
    from .views import views
    from .auth import auth
    from .reqst import reqst
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(reqst, url_prefix='/')

    from .models import Candidates

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #telling flask how we load a user
    @login_manager.user_loader
    def load_user(id):
        return Candidates.query.get(int(id))
    
    return app