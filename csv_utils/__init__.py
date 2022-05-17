import os

FILENAME = os.path.join('etc', 'data.csv')
HEADERS = {
    ('salary', 'name', 'surname', 'position', 'profile'): 'user',
    ('project_id', 'description'): 'task',
    ('task_id', 'comment'): 'comment',
    ('task_id', 'attachment'): 'attachment'
}
