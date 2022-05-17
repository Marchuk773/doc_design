from flask import Blueprint, jsonify
from . import comment_controller

comment = Blueprint("comment", __name__)


@comment.route('/comments')
def get_comments():
    comments = comment_controller.get_comments()
    return jsonify(comments)


@comment.route('/comment/<comment_id>')
def get_comment(comment_id):
    comment = comment_controller.get_comment(comment_id)
    return jsonify(comment)


@comment.route('/comment/read/csv')
def create_comments_from_csv():
    comment_controller.create_comments_from_csv()
    return jsonify('Success!')
