from flask import Blueprint, jsonify
from . import attachment_controller

attachment = Blueprint("attachment", __name__)


@attachment.route('/attachments')
def get_attachments():
    attachments = attachment_controller.get_attachments()
    return jsonify(attachments)


@attachment.route('/attachment/<attachment_id>')
def get_attachment(attachment_id):
    attachment = attachment_controller.get_attachment(attachment_id)
    return jsonify(attachment)


@attachment.route('/attachment/read/csv')
def create_attachments_from_csv():
    attachment_controller.create_attachments_from_csv()
    return jsonify('Success!')
