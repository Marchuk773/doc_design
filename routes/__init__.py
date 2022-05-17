from controllers.user_controller import UserController
from controllers.comment_controller import CommentController
from controllers.attachment_controller import AttachmentController
from controllers.task_controller import TaskController

from DAO.attachment_dao import AttachmentDAO
from DAO.task_dao import TaskDAO
from DAO.comment_dao import CommentDAO
from DAO.user_dao import UserDAO

from csv_utils.csv_reader import CSVReader

user_controller = UserController(UserDAO(), CSVReader())
comment_controller = CommentController(CommentDAO(), CSVReader())
attachment_controller = AttachmentController(AttachmentDAO(), CSVReader())
task_controller = TaskController(TaskDAO(), CSVReader())
