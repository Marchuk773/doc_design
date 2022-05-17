class TaskController:
    def __init__(self, controller_dao, file_reader):
        self.controller_dao = controller_dao
        self.file_reader = file_reader

    def get_task(self, task_id):
        return self.controller_dao.get_task(task_id)

    def get_tasks(self):
        return self.controller_dao.get_tasks()

    def create_task(self, **kwargs):
        return self.controller_dao.create_task(**kwargs)

    def create_tasks_from_csv(self):
        tasks = self.file_reader.read_csv('task')
        self.controller_dao.create_tasks(tasks)
