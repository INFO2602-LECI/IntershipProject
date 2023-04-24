import os
from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify
from .models import Pokemon, UserPokemon, User, db
from flask_login import LoginManager, current_user, login_user, login_required, logout_user


login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    flash('Unauthorized!')
    return redirect(url_for('login_page'))

def create_app():
  app = Flask(__name__, static_url_path='/static')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
  app.config['DEBUG'] = True
  app.config['SECRET_KEY'] = 'MySecretKey'
  app.config['PREFERRED_URL_SCHEME'] = 'https'
  db.init_app(app)
  login_manager.init_app(app)
  login_manager.login_view = "login_page"
  app.app_context().push()
  return app

app = create_app()

# Page Routes

#To update
@app.route("/", methods=['GET'])
def login():
    UserPokemons = UserPokemon.query.filter_by(user_id= current_user.id).all()
    get_pokemon = Pokemon.query.all()
    selected_pokemon = get_pokemon[0]
    return render_template("home.html",pokemon = get_pokemon, selected_pokemon = selected_pokemon,UserPokemons = UserPokemons)

@app.route("/login", methods=['GET'])
def login2():
    UserPokemons = UserPokemon.query.filter_by(user_id= current_user.id).all()
    get_pokemon = Pokemon.query.all()
    selected_pokemon = get_pokemon[0]
    return render_template("login.html",pokemon = get_pokemon, selected_pokemon = selected_pokemon,UserPokemons = UserPokemons)

@app.route("/app", methods=['GET'])
@login_required
def login_2():
    UserPokemons = UserPokemon.query.filter_by(user_id= current_user.id).all()
    get_pokemon = Pokemon.query.all()
    selected_pokemon = get_pokemon[0]
    print(get_pokemon)
    return render_template("home2.html",pokemon = get_pokemon, selected_pokemon = selected_pokemon,UserPokemons = UserPokemons)
@app.route("/app/<int:pokemon_id>", methods=['GET'])


# add @login_required decorator to require login
@login_required
def access_pokemon(pokemon_id):
    UserPokemons = UserPokemon.query.filter_by(user_id= current_user.id).all()
    pokemon = Pokemon.query.filter_by(id = int (pokemon_id)).first()
    print (Pokemon.id)
    pokemons = Pokemon.query.all()
    return render_template("home.html", pokemon = pokemons, selected_pokemon = pokemon,UserPokemons = UserPokemons)
def home_page(pokemon_id=1):
    #pass relevant data to template
    return render_template("home.html")

# Form Action Routes

@app.route('/signup', methods=['GET'])
def signup_page():
  return render_template('signup.html')


@app.route('/signup', methods=['GET'])
def signup_action():
  data = request.form  # get data from form submission
  newuser = User(username=data['username'], email=data['email'], password=data['password'])  # create user object
  try:
    db.session.add(newuser)
    db.session.commit()  # save user
    login_user(newuser)  # login the user
    flash('Account Created!')  # send message
    return redirect(url_for('signup.html'))  # redirect to homepage
  except Exception:  # attempted to insert a duplicate user
    db.session.rollback()
    flash("username or email already exists")  # error message
  return redirect(url_for('signup.html'))

@app.route('/login', methods=['POST'])
def login_1():
  data = request.form
  user = User.query.filter_by(username=data['username']).first()
  if user and user.check_password(data['password']):  # check credentials
    flash('Logged in successfully.')  # send message to next page
    login_user(user)  # login the user
    print(user)
    return redirect('/app')  # redirect to main page if login successful
  else:
    flash('Invalid username or password')  # send message to next page
  return redirect('/')


@app.route('/pokemon/<pokemon_id>', methods = ['POST'])
@login_required
def capture_pokemon2(pokemon_id):
  data = request.get_json()
  print(data)
  user = User.query.filter_by(id = current_user.id).first()
  user.catch_pokemon(pokemon_id, data['name'])
  return jsonify(success = "success"),200

@app.route('/rename-pokemon/<pokemon_id>', methods = ['POST'])
@login_required
def rename_pokemon(pokemon_id):
  data = request.get_json()
  print(data)
  user = User.query.filter_by(id = current_user.id).first()
  user.rename_pokemon(pokemon_id, data['name'])
  return jsonify(success = "success"),200

@app.route('/release-pokemon/<pokemon_id>', methods = ['GET'])
@login_required
def release_pokemon(pokemon_id):
  user = User.query.filter_by(id = current_user.id).first()
  user.release_pokemon(pokemon_id)
  return jsonify(success = "success"),200

@app.route("/logout", methods=['GET'])
def logout():
    UserPokemons = UserPokemon.query.filter_by(user_id= current_user.id).all()
    get_pokemon = Pokemon.query.all()
    selected_pokemon = get_pokemon[0]
    return render_template("home.html",pokemon = get_pokemon, selected_pokemon = selected_pokemon,UserPokemons = UserPokemons)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
