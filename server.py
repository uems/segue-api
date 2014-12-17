from flask import Flask, render_template, request, url_for, redirect
from flask.ext.restless import APIManager, ProcessingException
from database import db
from models import Person, Profile, Country, City, Proposal, Authorship
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

jwt = JWT(app)

#stub class. maybe in the future we would want to differentiate users acessing the api.
class User(object):
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      setattr(self, k, v)

@jwt.authentication_handler
def authenticate(username, password):
  if username == 'segue' and password == 'segue':
    return User(id=1, username='segue')
  return None

@jwt.user_handler
def load_user(payload):
  user = User(id=1, username='segue')
  return user

@jwt_required()
def auth_func(**kw):
  return True

apimanager = APIManager(app, flask_sqlalchemy_db=db)
apimanager.create_api(City,
  methods=['GET'],
  preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]),
  url_prefix=app.config['DEFAULT_URL_PREFIX'])
apimanager.create_api(Country,
  methods=['GET'],
  preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]),
  url_prefix=app.config['DEFAULT_URL_PREFIX'])
apimanager.create_api(Person,
  methods=['GET', 'POST', 'DELETE', 'PUT'],
  preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]),
  url_prefix=app.config['DEFAULT_URL_PREFIX'])
apimanager.create_api(Proposal,
  methods=['GET', 'POST', 'DELETE', 'PUT'],
  preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]),
  url_prefix=app.config['DEFAULT_URL_PREFIX'])
apimanager.create_api(Authorship,
  methods=['GET', 'POST', 'DELETE', 'PUT'],
  preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]),
  url_prefix=app.config['DEFAULT_URL_PREFIX'])

def init_app():
  db.init_app(app)

if __name__ == '__main__':		
  with app.app_context():
    init_app()
  app.run()
