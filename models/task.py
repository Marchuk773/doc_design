from app import db

class Task(db.Model):
    __tablename__ = "task"

    task_id = db.Column('id', db.Integer, primary_key=True)
    project_id = db.Column('projectId', db.Integer, nullable=False)
    description = db.Column('description', db.String(90))
    comments = db.relationship('Comment')
    attachments = db.relationship('Attachment')

class Comment(db.Model):
    __tablename__ = "comment"

    comment_id = db.Column('id', db.Integer, primary_key=True)
    task_id = db.Column('taskId', db.Integer, db.ForeignKey('task.id'))
    comment = db.Column('comment', db.String(90))

class Attachment(db.Model):
    __tablename__ = "attachment"

    attachment_id = db.Column('id', db.Integer, primary_key=True)
    task_id = db.Column('taskId', db.Integer, db.ForeignKey('task.id'))
    attachment = db.Column('attachment', db.String(90))
