# -*- coding: utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
migrate = Migrate(app, db)


import example_app_01.admin
