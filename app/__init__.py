from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='public', static_url_path='/public')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///database.db'
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)

db = SQLAlchemy(app)