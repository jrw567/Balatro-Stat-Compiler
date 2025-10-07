from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///balatrostatdb.db'
db = SQLAlchemy(app, session_options={"autoflush": False})
with app.app_context():
        db.create_all()