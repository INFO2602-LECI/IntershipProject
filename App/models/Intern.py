from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class Intern(User):


    def __init__(self, username, password):
        super().__init__(self, username, password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
            'name': self.name
        }

   
