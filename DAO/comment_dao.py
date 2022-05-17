from app import db
from models.task import Comment


class CommentDAO:
    def create_comment(**kwargs):
        new_comment = Comment(**kwargs)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment

    def get_comment(self, comment_id):
        comment = Comment.query.filter_by(comment_id=comment_id).first()
        return comment

    def get_comments(self):
        comments = Comment.query.all()
        return comments

    def create_comments(self, comments_values):
        comments = [Comment(**values) for values in comments_values]
        db.session.add_all(comments)
        db.session.commit()
