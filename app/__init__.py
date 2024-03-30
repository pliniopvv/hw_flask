from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__, static_folder='public', static_url_path='/public')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)