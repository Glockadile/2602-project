from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#816020350

## Create a User Model
## must have set_password, check_password and to Dict
class User(db.Model): #code obtained from lab 5
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
      return {
        #"id": self.id,
        "username": self.username,
        "email": self.email,
        "password":self.password
      }
    
    #To String method
    def __repr__(self):
        return '<User {}>'.format(self.username)  

#816020350
## Create a Pokemon Model
class Players(db.Model):
    first_name= db.Column(db.String(80), nullable=False)
    second_name= db.Column(db.String(80), nullable=False)
    assists= db.Column(db.Integer, nullable=False)
    clean_sheets= db.Column(db.Integer, nullable=False)
    form= db.Column(db.Integer, nullable=False)
    goals_conceded= db.Column(db.Integer, nullable=False)
    goals_scored= db.Column(db.Integer, nullable=False)
    minutes= db.Column(db.Integer, nullable=False)
    penalties_saved= db.Column(db.Integer, nullable=False)
    red_cards= db.Column(db.Integer, nullable=False)
    saves= db.Column(db.Integer, nullable=False)
    yellow_cards= db.Column(db.Integer, nullable=False)


    def toDict(self):
      return {
        "first_name": self.first_name,
        "second_name": self.second_name,
        "assists": self.assists,
        "clean_sheets": self.clean_sheets,
        "form": self.form,
        "goals_conceded": self.goals_conceded,
        "goals_scored": self.goals_scored,
        "minutes": self.minutes,
        "penalties_saved": self.penalties_saved,
        "red_cards": self.red_cards,
        "yellow_cards": self.yellow_cards,
      }
      #816020350