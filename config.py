from datetime import timedelta

class Config(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = ''

  APP_NAME = 'SEGUE'
  SECRET_KEY = '\xd0\x8d\xc7\x88\xc0]+L\x18D\xe6\xd7\x15c\x8eo\xcd\xd5\x05\xd8\xdb\xe9\xb2\xaf\xb6e\x9b\xda\x93\xad\xce\xfb'
  DEFAULT_URL_PREFIX = '/api/v1'
  JWT_EXPIRATION_DELTA = timedelta(days=1)
  JWT_AUTH_URL_RULE = DEFAULT_URL_PREFIX + '/auth'
  #SECURITY_REGISTERABLE = True
  #SECURITY_RECOVERABLE = True
  #SECURITY_TRACKABLE = True
  #SECURITY_PASSWORD_HASH = 'sha512_crypt'
  #SECURITY_PASSWORD_SALT = 'add_salt'

class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/segue'

class DevelopmentConfig(Config):
  #SQLALCHEMY_DATABASE_URI = 'sqlite:///dumps/segue.sqlite'
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/segue'
  DEBUG = True

class TestingConfig(Config):
  #SQLALCHEMY_DATABASE_URI = 'sqlite:///dumps/segue.sqlite'
  TESTING = True

