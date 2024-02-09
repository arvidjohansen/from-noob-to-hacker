# app.py

import sys
from datetime import datetime, timedelta
from enum import Enum
from flask import Flask, render_template, redirect, request
from flask import flash, Response, session
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from queue import Queue
from pytube import YouTube
from sqlalchemy.sql import func
from utilities import time_since, default_if_none
from random import choice
from wtforms import TextAreaField
from uuid import uuid4
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config["DOWNLOAD_FOLDER"] = "downloads"
db = SQLAlchemy(app)
app.jinja_env.filters['time_since'] = time_since
app.jinja_env.filters['default_if_none'] = default_if_none


users = {}
messages = []
message_queues = {}

@app.route('/')
def index():
    session['id'] = str(uuid4())
    return render_template('chatserver2.html')

@app.route('/home')
def home():
    return redirect(url_for('index'))


@app.route('/cam')
def cam():
    session['id'] = str(uuid4())
    return render_template('camdetector.html')


@app.route('/connect')
def connect():
    animal_names = ['Lion', 'Tiger', 'Elephant', 'Deer', 'Rabbit']
    username = 'anonymous-' + choice(animal_names)
    users[session['id']] = username
    message_queues[username] = Queue()
    return Response(event_stream(username), mimetype='text/event-stream')

@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    username = request.form.get('username')
    messages.append({'username': username, 'message': message, 'timestamp': datetime.now()})
    for user, queue in message_queues.items():
        queue.put(message)
    return '', 204

def event_stream(username):
    while True:
        message = message_queues[username].get()
        print(f'Got message: {message}')
        yield f'data: {message}\n\n'


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
        
        
