from database import db

class City(db.Model):
  __tablename__ = 'cities'
  
  id = db.Column(db.Integer, primary_key=True)
  state = db.Column(db.String(2), nullable=False)
  name = db.Column(db.String(50), nullable=False)
  latitude = db.Column(db.Float(53), nullable=False)
  longitude = db.Column(db.Float(53), nullable=False)

class Country(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  cctld = db.Column(db.String(2), nullable=False)
  iso = db.Column(db.Integer, nullable=False)
  
class Profile(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  content = db.Column(db.Text)

class Person(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  email = db.Column(db.String(255))
  organization = db.Column(db.String(255))
  curriculum = db.Column(db.Text)
  photo = db.Column(db.String(255))
  document = db.Column(db.String(255))
  passport = db.Column(db.String(255))
  
  country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
  city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
  country = db.relationship(Country)
  city = db.relationship(City)
  
  phone = db.Column(db.String(255))
  
  # Male, Female, Undefined
  sex = db.Column(db.Enum(u'M',u'F',u'U',name='sex_enum'))
  password = db.Column(db.String(100))
  
  profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
  profile = db.relationship(Profile)

class Authorship(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id'))
  person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
  involvement = db.Column(db.String(100))
  confirmed = db.Column(db.Boolean)
  main = db.Column(db.Boolean)
  showed_up = db.Column(db.Boolean)
  
class Proposal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text)
  abstract = db.Column(db.Text)
  description = db.Column(db.Text)
  video_authorization = db.Column(db.Boolean)
  language = db.Column(db.String(100))
  level = db.Column(db.String(100))
  authors = db.relationship(Authorship)

