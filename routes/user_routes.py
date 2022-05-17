from flask import Blueprint, jsonify
from . import user_controller

user = Blueprint("user", __name__)


@user.route('/users')
def get_users():
    users = user_controller.get_users()
    return jsonify(users)


@user.route('/user/<user_id>')
def get_user(user_id):
    user = user_controller.get_user(user_id)
    return jsonify(user)


@user.route('/user/read/csv')
def create_users_from_csv():
    user_controller.create_users_from_csv()
    return jsonify('Success!')
