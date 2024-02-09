# app.py

import sys
from enum import Enum
from flask import Flask, render_template, redirect, request
from flask import flash
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from pytube import YouTube
from sqlalchemy.sql import func
from utilities import time_since, default_if_none
from wtforms import TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config["DOWNLOAD_FOLDER"] = "downloads"
db = SQLAlchemy(app)
app.jinja_env.filters['time_since'] = time_since
app.jinja_env.filters['default_if_none'] = default_if_none



if __name__ == '__main__':
    with app.app_context():
        if len(sys.argv) > 1:
            if sys.argv[1] == 'resetdb':
                ans = input('Are you sure you want to reset the database? (y/n): ')
                if ans == 'y':
                    # reset database
                    db.drop_all()
                    print('Database reset successful.')
        db.create_all()
        app.run(debug=True)
        
        
