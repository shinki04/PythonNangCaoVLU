import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Tạo bảng
@app.before_first_request
def create_tables():
    db.create_all()
