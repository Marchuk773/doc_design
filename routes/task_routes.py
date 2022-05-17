from flask import Blueprint, jsonify
from . import task_controller

task = Blueprint("task", __name__)


@task.route('/tasks')
def get_tasks():
    tasks = task_controller.get_tasks()
    return jsonify(tasks)


@task.route('/task/<task_id>')
def get_task(task_id):
    task = task_controller.get_task(task_id)
    return jsonify(task)


@task.route('/task/read/csv')
def create_tasks_from_csv():
    task_controller.create_tasks_from_csv()
    return jsonify('Success!')
