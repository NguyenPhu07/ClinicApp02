from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = '5y45yert545*3434434tytrt567^^*&^&&($#%'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:phutv123@localhost/clinicapv2?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app=app)
login = LoginManager(app=app)


