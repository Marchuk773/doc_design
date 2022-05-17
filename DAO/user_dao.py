from app import db
from models.user import User


class UserDAO:
    def create_user(**kwargs):
        new_user = User(**kwargs)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_user(self, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        return user

    def get_users(self):
        users = User.query.all()
        return users

    def create_users(self, users_values):
        users = [User(**values) for values in users_values]
        db.session.add_all(users)
        db.session.commit()
