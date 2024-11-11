import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

Role.users = db.relationship('User', backref='role')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        db.drop_all()  # Optional: Use this line only if you want to drop existing tables
        db.create_all()

        admin_role = Role(name='Admin')
        mod_role = Role(name='Moderator')
        user_role = Role(name='User')
        
        user_john = User(username='john', role=admin_role)
        user_susan = User(username='susan', role=user_role)
        user_david = User(username='david', role=user_role)

        db.session.add(admin_role)
        db.session.add(mod_role)
        db.session.add(user_role)
        db.session.add(user_john)
        db.session.add(user_susan)
        db.session.add(user_david)

        admin_role.name = 'Administrator'
        db.session.add(admin_role)

        db.session.commit()

        print("Database created and data added.")