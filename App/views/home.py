from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from App.models import InternAdmin, Intern, Ship
from datetime import datetime

from.index import index_views

from App.controllers import (
    get_admin, 
    get_ship,
    get_all_ship,
    get_all_ship_json,
    create_ship,
    update_ship_name,
    update_desc,
    update_location,
    update_spots,
    update_enrolled,
    del_ship
)

home_views = Blueprint('home_views', __name__, template_folder='../templates')


# Home Page
#----------------------------------------------------------------------------
@home_views.route('/home', methods=['GET'])
@login_required
def homepage():
    chosen= -1
    ships = get_all_ship()
    id = current_user.get_id()#get current user id
    admin = get_admin(id)#get the admin object
    name = admin.name #get admin name
    return render_template('home.html', admin = name, scrollers= ships, chosen=chosen)

# Scroll Bar Setup
# ----------------------------------------------------------------------------------
@home_views.route('/home/<int:ship_id>', methods=['GET'])
@login_required
def homepage_withships(ship_id):
    chosen= get_ship(ship_id)
    if chosen== None:
        chosen=-1
    ships = get_all_ship()
    id = current_user.get_id()#get current user id
    admin = get_admin(id)#get the admin object
    name = admin.name #get admin name
    return render_template('home.html', admin = name, scrollers= ships, chosen=chosen)
    
# Create Internship - Working
# ----------------------------------------------------------------------------------
@home_views.route('/home', methods=['POST'])
@login_required
def make_internship():
    data = request.form
    internship  = create_ship(data['name'], data['desc'], data['location'],data['date_time'], data['openspots'] )
    # internship  = create_internship(data['name'], data['desc'], data['location'], data['openspots'], data['date_time'])
    # internship  = Internship(data['name'], data['desc'], data['location'], data['openspots'], data['date_time'])
    if internship!= None:
        flash(f"Internship {data['name']} created!")
    else:
        flash(f"Internship not created!")
    return redirect('/home')

# UPDATE INTERNSHIP ROUTES
# Update Internship Name
# ----------------------------------------------------------------------------------
@home_views.route('/update_name/<int:ship_id>', methods=['POST'])
@login_required
def name_change(ship_id):
    ship= get_ship(ship_id)
    data = request.form
    ship = update_name(ship_id,data['name'])
    if ship!= None:
        flash(f"Internship {data['name']} changed!")
    else:
        flash(f"Name not changed!")
    return redirect('/home/ship_id')   

@home_views.route('/update_desc/<int:ship_id>', methods=['POST'])
@login_required
def desc_change(ship_id):
    ship= get_ship(ship_id)
    data = request.form
    ship = update_desc(ship_id,data['desc'])
    if ship!= None:
        flash(f"Internship Description changed!")
    else:
        flash(f"Description not changed!")
    return redirect('/home/ship_id')


@home_views.route('/update_location/<int:ship_id>', methods=['POST'])
@login_required
def location_change(ship_id):
    ship= get_ship(ship_id)
    data = request.form
    ship = update_location(ship_id,data['location'])
    if ship!= None:
        flash(f"Internship Location changed!")
    else:
        flash(f"Location not changed!")
    return redirect('/home/ship_id')


    
# Logout
# --------------------------------------------------------------------------
@home_views.route("/home/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    flash('Logged Out')
    return redirect('/')

