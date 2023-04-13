from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user

from.index import index_views

from App.controllers import (
    create_user,
    authenticate, 
    get_all_users,
    get_all_users_json,
)

home_views = Blueprint('home_views', __name__, template_folder='../templates')

pass 

@home_views.route('/home', methods=['GET'])
def homepage():
    return render_template('home.html')

