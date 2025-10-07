from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///balatrostatdb.db'
db = SQLAlchemy(app, session_options={"autoflush": False})

engine = create_engine('sqlite:///balatrostatdb.db', connect_args={"check_same_thread": False}, poolclass=StaticPool)