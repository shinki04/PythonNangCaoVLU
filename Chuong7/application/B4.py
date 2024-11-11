import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
basedir = os.path.abspath(os.path. dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__= 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    users = db.relationship('User',backref= 'role')
    def __repr__(self) :
        return '<Role %r>' % self.name

class User(db.Model) :
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    def __repr__(self) :    
        return '<User %r>' % self.username
    
    
    
if __name__ == "__main__":
    app.run(debug=True)







