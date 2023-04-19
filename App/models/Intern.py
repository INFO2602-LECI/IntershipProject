from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import User, user

class Intern(User):
    def __init__(self, username, password, name, course):
        super().__init__(self, username, password)
        self.name= name
        self.course= course

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'course': self.course
            # 'name': self.name
        }

    def add_course(self, course):
        self.courses.append(course)
        db.session.add(self)
        db.session.commit()

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            db.session.add(self)
            db.session.commit()

   
