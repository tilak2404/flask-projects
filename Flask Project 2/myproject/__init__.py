import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

Login_Manager=LoginManager()

app=Flask(__name__)

app.config['SECRET_KEY']='mykey'
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
app.db=db
Migrate(app,db)

Login_Manager.init_app(app)
Login_Manager.login_view='login'


