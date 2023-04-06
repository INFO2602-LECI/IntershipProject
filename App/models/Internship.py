from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import User, user, Intern, InternAdmin
from datetime import datetime

class InternAdmin(db.Model):


    def __init__(self, name, desc, location, datetime, openspots, enrolled):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(120), nullable=False, unique=False)
    desc =  db.Column(db.String(120), nullable=True)
    location = db.Column(db.String(120), nullable=False)
    datetime = db.Column(db.Date, nullable=False)
    openspots = db.Column(db.Integer, nullable=True)
    enrolled = db.Column(db.Integer, nullable=True)


    def get_json(self):
        return{
            'Name': self.name
            'Description': self.desc,
            'Location': self.location,
            'Date and Time': self.datetime,
            'Spots Remaing': self.openspots,
            'Enrolled': self.enrolled
        }
