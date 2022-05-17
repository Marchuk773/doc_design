from app import db
from models.task import Attachment


class AttachmentDAO:
    def create_attachment(**kwargs):
        new_attachment = Attachment(**kwargs)
        db.session.add(new_attachment)
        db.session.commit()
        return new_attachment

    def get_attachment(self, attachment_id):
        attachment = Attachment.query.filter_by(attachment_id=attachment_id).first()
        return attachment

    def get_attachments(self):
        attachments = Attachment.query.all()
        return attachments

    def create_attachments(self, attachments_values):
        attachments = [Attachment(**values) for values in attachments_values]
        db.session.add_all(attachments)
        db.session.commit()
