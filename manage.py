from flask.ext.script import Manager
from server import app, db
import os

manager = Manager(app)

db.init_app(app)

@manager.command
def create_tables():
  "Create the tables inside the database"
  db.create_all()

@manager.command
def drop_all():
  "Drops all data (USE WITH CAUTION)"
  db.drop_all()
  
@manager.command
def populate():
  "Populate the tables 'cities' and 'country' with standard data"
  os.system("sudo -u postgres psql segue < ./docs/country_city_data.sql")

if __name__ == '__main__':
  manager.run()