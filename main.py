from flask import Flask
import click
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memory.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) )
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) )

@app.cli.command("mydb")
@click.argument("updown", default="up")
def create_db(updown):
    if updown == "up":
        print("Creating database")
        db.create_all()
        print("Database Created")
    elif updown == "down":
        print("Dropping database")
        db.drop_all()
        print("Database Dropped")


@app.route("/")
def home():
    return "Hello"
