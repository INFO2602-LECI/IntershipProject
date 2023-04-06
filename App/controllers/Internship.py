from App.models import  Internshipship
from App.database import db


def get_internship(id):
    return Internship.query.get(id)

def get_all_internship():
    return Internship.query.all()

def get_all_internship_json():
    internships = Internship.query.all()
    if not internships:
        return []
    internships = [internship.get_json() for internship in internships]
    return internships

def update_internship(id, username):
    internship = get_internship(id)
    if internship:
        internship.username = username
        db.session.add(internship)
        return db.session.commit()
    return None

#Internship Controllers
# --------------------------------------------------------------------------------
def create_internship(name, desc, location, datetime, openspots, enrolled)
    # datetime(year, month, day, hour, minute, second, microsecond)
    # b = datetime(2022, 12, 28, 23, 55, 59, 342380)
    internship = Internship(name=name, desc=desc, location=location, datetime = datetime, openspots = openspots, enrolled = enrolled)
    db.session.add(internship)
    db.session.commit()
    return internship
    
# Update Controllers
# --------------------------------------------------------------------------------------
#Name 
def update_name(id, name):
    internship = get_internship(id)
    if internship:
        internship.name = name
        db.session.add(internship)
        return db.session.commit()
    return None

#Description 
def update_desc(id, desc):
    internship = get_internship(id)
    if internship:
        internship.des = desc
        db.session.add(internship)
        return db.session.commit()
    return None
    
# Location
def update_location(id, loc):
    internship = get_internship(id)
    if internship:
        internship.location = loc
        db.session.add(internship)
        return db.session.commit()
    return None  

# Open Spots
def update_spots(id, spots):
    internship = get_internship(id)
    if internship:
        internship.openspots = spots
        db.session.add(internship)
        return db.session.commit()
    return None  

# Enrolled
def update_enrolled(id, er):
    internship = get_internship(id)
    if internship:
        internship.enrolled = er
        db.session.add(internship)
        return db.session.commit()
    return None