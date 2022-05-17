from app import app, db

from routes.main_route import main_
from routes.task_routes import task
from routes.user_routes import user
from routes.comment_routes import comment
from routes.attachment_routes import attachment


def register_routes(app):
    app.register_blueprint(main_)
    app.register_blueprint(task)
    app.register_blueprint(comment)
    app.register_blueprint(user)
    app.register_blueprint(attachment)


def main():
    register_routes(app)
    db.create_all()
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
