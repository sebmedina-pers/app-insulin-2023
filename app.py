import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db

# load env variables
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{os.getenv('DB_PW')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = os.getenv("APP_KEY")

db.init_app(app)


# if __name__ == "__main__":
#     app.run(host="localhost", port=5000)