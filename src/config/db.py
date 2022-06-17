from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:cambodia@localhost/dborf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# if __name__ == 'createdb':
#     db.reflect()
#     db.drop_all()
#     db = SQLAlchemy(app)