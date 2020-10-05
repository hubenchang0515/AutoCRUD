from flask import Flask
import os

from .database import db, filterDict, convertDbModel
from .app import app, getJson

def init(sql_url:str):
    app.config['SQLALCHEMY_DATABASE_URI'] = sql_url
    #app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = os.urandom(64)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app