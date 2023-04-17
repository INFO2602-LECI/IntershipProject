from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user
import datetime

from.index import index_views

from App.controllers import (
    authenticate,
    get_admin, 
    create_internship,
    get_all_internship,
    get_all_internship_json,
)

home_views = Blueprint('home_views', __name__, template_folder='../templates')
# Home Page
#----------------------------------------------------------------------------
@home_views.route('/home', methods=['GET'])
@jwt_required()
def homepage():
    # internships = get_all_internship()
    id = current_user.get_id()
    admin = get_admin(id)
    return render_template('home.html', admin = admin)

# Logout
# --------------------------------------------------------------------------
@home_views.route('/home/logout', methods=['POST'])
@jwt_required()
def logout():
    current_user = ''
    return redirect ('/login')

# @home_views.route("/home/logout", methods=["POST"])
# @jwt_required()
# def logout():
#     jti = get_jwt()["jti"]
#     jwt_redis_blocklist.set(jti, "", ex=ACCESS_EXPIRES)
#     return redirect ('/login')
    # missing authorization header appeared

# current error 
# File "/workspace/IntershipProject/App/controllers/Internship.py", line 10, in get_all_internship
#     return Internship.query.all()
# AttributeError: module 'App.models.Internship' has no attribute 'query'
    
@home_views.route('/home', methods=['POST'])
@jwt_required()
def create_internship():
    data = request.form
    internship  = create_internship(data['name'], data['desc'], data['location'], data['datetime'], data['openspots'], data['enrolled'])
    if internship:
        flash(f"Internship {data['name']} created!")
    else:
        flash(f"Internship not created!")


