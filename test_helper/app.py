from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///some_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(10), nullable=False)


some_table = TestTable(value='some_val')
with app.app_context():
    db.session.add(some_table)
    db.session.commit()
