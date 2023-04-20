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


# current error 
# File "/workspace/IntershipProject/App/controllers/Internship.py", line 10, in get_all_internship
#     return Internship.query.all()
# AttributeError: module 'App.models.Internship' has no attribute 'query'

    
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
    
@home_views.route('/update/<int:ship_id>', methods=['POST'])
@login_required
def namechange(ship_id):
    ship= get_ship(ship_id)
    data = request.form
    ship = change_name(ship_id,data['name'])
    if ship!= None:
        flash(f"Internship {data['name']} changed!")
    else:
        flash(f"Name not changed!")
    return redirect('/home/ship_id')


# Logout
# --------------------------------------------------------------------------
@home_views.route("/home/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    flash('Logged Out')
    return redirect('/')

