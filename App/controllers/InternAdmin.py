from App.models import InternAdmin, Internship
from App.database import db

def create_admin(id, username, name):
    if admin:
        admin.username = username
        db.session.add(admin)
        return db.session.commit()
    return None

def get_admin_by_username(username):
    return Admin.query.filter_by(username=username).first()

def get_admin_by_name(name):
    return Admin.query.filter_by(name=name).first()

def get_admin(id):
    return InternAdmin.query.get(id)

def get_all_admin():
    return InternAdmin.query.all()

def get_all_admin_json():
    admins = InternAdmin.query.all()
    if not admins:
        return []
    admins = [admin.get_json() for admin in admins]
    return admins

def update_admin(id, username):
    admin = get_admin(id)
    if admin:
        admin.username = username
        db.session.add(admin)
        return db.session.commit()
    return None

#Internship Controllers
# --------------------------------------------------------------------------------
def create_internship(name, desc, location, date_time, openspots, enrolled):
    # datetime(year, month, day, hour, minute, second, microsecond)
    # b = datetime(2022, 12, 28, 23, 55, 59, 342380)
    internship = Internship(name=name, desc=desc, location=location, date_time = date_time, openspots = openspots, enrolled = enrolled)
    db.session.add(internship)
    db.session.commit()
    return internship
    
def change_name(id, name):
    internship = get_internship(id)
    if internship:
        internship = update_name(id,name)
        return internship
    return None   

def change_desc(id, desc):
    internship = get_internship(id)
    if internship:
        internship = update_desc(id,desc)
        return internship
    return None   

def change_location(id, loc):
    internship = get_internship(id)
    if internship:
        internship = update_location(id,loc)
        return internship
    return None
  
def change_spots(id, spots):
    internship = get_internship(id)
    if internship:
        internship = update_spots(id, spots)
        return internship
    return None
  
def change_enrolled(id, er):
    internship = get_internship(id)
    if internship:
        internship = update_enrolled(id,loc)
        return internship
    return None
  
