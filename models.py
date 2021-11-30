from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Project Title", db.String())
    date = db.Column("Project Date", db.DateTime)
    description = db.Column("Project Description", db.Text)
    skills = db.Column("Skills Used", db.Text)
    url = db.Column('GitHub Repo Link', db.Text)

    def __repr__(self):
        return f"""\n----------
                \Project Title: {self.title}
                \r----------
                \Date: {self.date}
                \r----------
                \Description: {self.description}
                \r----------
                \Skills: {self.skills}
                \r----------
                \rGithub Repo Link: {self.url}
                 f"""----------
