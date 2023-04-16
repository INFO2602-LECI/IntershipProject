from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user
import datetime

from.index import index_views

from App.controllers import (
    authenticate, 
    create_internship,
    get_all_internship,
    get_all_internship_json
)

home_views = Blueprint('home_views', __name__, template_folder='../templates')

@home_views.route('/home', methods=['GET'])
def homepage():
    internships = get_all_internship
    return render_template('home.html', internships= internships)

    
@home_views.route('/home', methods=['POST'])
def create_internship():
    data = request.form
    internship  = create_internship(data['name'], data['desc'], data['location'], data['datetime'], data['openspots'], data['enrolled'])
    if internship:
        flash(f"Internship {data['username']} created!")
    create_user(data['username'], data['password'], data['name'])
    return redirect('/home')

