from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
file_path = os.path.abspath(os.getcwd())+"\database.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path

db = SQLAlchemy(app)

#two tables for todo and user login table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer) #this can be foreign key

if __name__ == '__main__':
    app.run(debug=True)

    #need to check and dowload sqlite3