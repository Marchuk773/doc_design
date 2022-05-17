from flask import Blueprint

main_ = Blueprint("main", __name__)


@main_.route('/')
def index():
    return "Jira :)"
