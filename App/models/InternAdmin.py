from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import User, user

class InternAdmin(User):


    def __init__(self, username, password, name):
        super().__init__(self, username, password)
        # name =  db.Column(db.String(120), nullable=False, unique=False)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'name': self.name
        }