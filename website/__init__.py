from calendar import c
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager


#from website.models import Candidates

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']= 'elif is here'  #encrypt or secure the cookies and session data related to our website
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Eyh23894@localhost:5432/HRMS_db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    migrate = Migrate(app, db)

    from .views import views 
    from .auth import auth
    from .reqst import reqst

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(reqst, url_prefix='/')

    from .models import Candidates

    login_manager =LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    #telling flask how we load a user
    @login_manager.user_loader
    def load_user(id):
        return Candidates.query.get(int(id)) 
    
    return app

