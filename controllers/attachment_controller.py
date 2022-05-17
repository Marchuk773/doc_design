class AttachmentController:
    def __init__(self, attachment_dao, file_reader):
        self.attachment_dao = attachment_dao
        self.file_reader = file_reader

    def get_attachment(self, attachment_id):
        return self.attachment_dao.get_attachment(attachment_id)

    def get_attachments(self):
        return self.attachment_dao.get_attachments()

    def create_attachment(self, **kwargs):
        return self.attachment_dao.create_attachment(**kwargs)

    def create_attachments_from_csv(self):
        attachments = self.file_reader.read_csv('attachment')
        self.attachment_dao.create_attachments(attachments)
