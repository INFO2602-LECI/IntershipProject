from App.models import InternAdmin, Ship
from App.database import db

# testing
# def create_ship(name, desc, location, date_time. ,openspots):
#     ship = Ship(name=name, desc=desc, location=location, date_time=date_time, openspots = openspots )
#     if ship:
#         db.session.add(ship)
#         return db.session.commit()
#     return None
    
#Ship Controllers
# --------------------------------------------------------------------------------
def create_ship(name, desc, location, date_time, openspots):
    ship = Ship(name=name, desc=desc, location=location, date_time = date_time, openspots = openspots)
    if ship:
        db.session.add(ship)
        db.session.commit()
        return ship
    return None
    # datetime(year, month, day, hour, minute, second, microsecond)
    # b = datetime(2022, 12, 28, 23, 55, 59, 342380)
    
def get_ship(id):
    return Ship.query.get(id)

def get_all_ship():
    return Ship.query.all()

def get_all_ship_json():
    ships = Ship.query.all()
    if not ships:
        return []
    ships = [ship.get_json() for ship in ships]
    return ships

def get_ship_by_name(name):
    return Ship.query.filter_by(name=name).first()

# def update_ship_name(id, name):
#     ship = get_ship(id)
#     if ship:
#         ship.name = name
#         db.session.add(ship)
#         return db.session.commit()
#     return None

    
# Update Controllers
# --------------------------------------------------------------------------------------
#Name 
def update_ship_name(id, name):
    ship = get_ship(id)
    if ship:
        ship.name = name
        db.session.add(ship)
        db.session.commit()
        return ship
    return None

#Description 
def update_desc(id, desc):
    ship = get_ship(id)
    if ship:
        ship.desc = desc
        db.session.add(ship)
        db.session.commit()
        return ship
    return None
    
# Location
def update_location(id, loc):
    ship = get_ship(id)
    if ship:
        ship.location = loc
        db.session.add(ship)
        db.session.commit()
        return ship
    return None  

# Date and Time
def update_datetime(id, date_time):
    ship = get_ship(id)
    if ship:
        ship.date_time = date_time
        db.session.add(ship)
        db.session.commit()
        return ship
    return None  

# Open Spots
def update_spots(id, spots):
    ship = get_ship(id)
    if ship:
        ship.openspots = spots
        db.session.add(ship)
        db.session.commit()
        return ship
    return None  

# # Enrolled
# def update_enrolled(id, er):
#     ship = get_ship(id)
#     if ship:
#         ship.enrolled = er
#         db.session.add(ship) 
#         db.session.commit()
#         return ship
#     return None

# Delete
def del_ship(id):
    ship = get_ship(id)
    if ship:
        db.session.delete(ship)
        db.session.commit()
        return ship
    return None

