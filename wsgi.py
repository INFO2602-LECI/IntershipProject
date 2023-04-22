import click
import csv
from App import db, User, Pokemon, UserPokemon
from App import app

@app.cli.command("init", help="Creates and initializes the database")
def initialize():
  db.drop_all()
  db.create_all()
  bob = User("bob", "bob@mail.com", "bobpass")
  db.session.add(bob)
  db.session.commit()
  
  with open('Internship-data.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

      pokemon = Pokemon(name=row['name'], description=row['description'], location=row['location'], stipend=row['stipend'], datetime=row['datetime'], runtime=row['runtime'], openspots=row['openspots'], enrolled=row['enrolled'])
      db.session.add(pokemon)
    db.session.commit()
  print('database initialized')
