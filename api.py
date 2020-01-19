from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/Users/xxchr/Desktop/Project/RESTfulApi'

db - SQLAlchemy(app)

class User(db.Model):
    id = db.col

if __name__ == '__main__':
    app.run(debug=True)