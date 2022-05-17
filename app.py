from os import getenv
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from utils.json_encoder import CustomJSONEncoder

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{host}/{db_name}'.format(
    user=getenv('DB_USER'),
    password=getenv('DB_PASSWORD'),
    host=getenv('DB_HOSTNAME'),
    db_name=getenv('DB_SCHEMA')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json_encoder = CustomJSONEncoder

db = SQLAlchemy(app)
