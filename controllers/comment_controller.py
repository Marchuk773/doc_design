class CommentController:
    def __init__(self, comment_dao, file_reader):
        self.comment_dao = comment_dao
        self.file_reader = file_reader

    def get_comment(self, comment_id):
        return self.comment_dao.get_comment(comment_id)

    def get_comments(self):
        return self.comment_dao.get_comments()

    def create_comment(self, **kwargs):
        return self.comment_dao.create_comment(**kwargs)

    def create_comments_from_csv(self):
        comments = self.file_reader.read_csv('comment')
        self.comment_dao.create_comments(comments)
