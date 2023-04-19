from App.models import Intern
from App.database import db

def get_intern(id):
    return Intern.query.get(id)

def get_all_intern():
    return Internship.query.all()

def get_all_intern_json():
    intern = Intern.query.all()
    if not intern:
        return []
    intern= [intern.get_json() for intern in intern]
    return intern

def update_intern(id, username):
    intern = get_intern(id)
    if intern:
        intern.username = username
        db.session.add(intern)
        return db.session.commit()
    return None

def create_intern(self, username, password, name, course):
        intern = Intern(username=username, password=password, name=name, course=course)
        db.session.add(intern)
        db.session.commit()
        return intern

def create_intern(self, username, password, name, course):
        intern = Intern(username=username, password=password, name=name, course=course)
        db.session.add(intern)
        db.session.commit()
        return intern

def update_intern(self, id, username):
        intern = self.get_intern(id)
        if intern:
            intern.username = username
            db.session.add(intern)
            db.session.commit()
            return True
        return False

def delete_intern(self, id):
        intern = self.get_intern(id)
        if intern:
            db.session.delete(intern)
            db.session.commit()
            return True
        return False



