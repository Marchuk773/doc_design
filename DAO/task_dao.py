from app import db
from models.task import Task


class TaskDAO:
    def create_task(**kwargs):
        new_task = Task(**kwargs)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    def get_task(self, task_id):
        task = Task.query.filter_by(task_id=task_id).first()
        return task

    def get_tasks(self):
        tasks = Task.query.all()
        return tasks

    def create_tasks(self, tasks_values):
        tasks = [Task(**values) for values in tasks_values]
        db.session.add_all(tasks)
        db.session.commit()
