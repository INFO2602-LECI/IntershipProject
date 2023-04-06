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

# @home_views.route('/home', methods=['GET'])
# def homepage():
#     return render_template('home.html')

# @home_views.route('/api/users', methods=['GET'])
# def get_users_action():
#     users = get_all_users_json()
#     return jsonify(users)

# @home_views.route('/api/users', methods=['POST'])
# def create_user_endpoint():
#     data = request.json
#     create_user(data['username'], data['password'])
#     return jsonify({'message': f"user {data['username']} created"})

# @home_views.route('/api/login', methods=['POST'])
# def user_login_api():
#   data = request.json
#   token = authenticate(data['username'], data['password'])
#   if not token:
#     return jsonify(message='bad username or password given'), 401
#   return jsonify(access_token=token)

# @home_views.route('/api/identify', methods=['GET'])
# @jwt_required()
# def identify_user_action():
#     return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})

# @home_views.route('/users', methods=['POST'])
# def create_user_action():
#     data = request.form
#     flash(f"User {data['username']} created!")
#     create_user(data['username'], data['password'])
#     return redirect(url_for('home_views.get_user_page'))

# @home_views.route('/static/users', methods=['GET'])
# def static_user_page():
#   return send_from_directory('static', 'static-user.html')