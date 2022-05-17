from app import db

class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    surname = db.Column('surname', db.String(45))
    salary = db.Column('salary', db.Float)
    position = db.Column('position', db.String(45))
    profile = db.Column('profile', db.String(45))
