# chatserver.py
from flask import Flask, redirect, render_template, request, url_for
from flask_socketio import SocketIO, emit, join_room
from random import choice
from datetime import datetime, timedelta

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}
messages = []

@app.route('/')
def index():
    return render_template('chatserver.html')

@app.route('/home')
def home():
    return redirect(url_for('index'))


@socketio.on('connect')
def connect():
    animal_names = ['Lion', 'Tiger', 'Elephant', 'Deer', 'Rabbit']
    username = 'anonymous-' + choice(animal_names)
    users[request.sid] = username
    emit('user connected', {'username': username}, broadcast=True)
    emit('load messages', [msg for msg in messages if msg['timestamp'] > datetime.now() - timedelta(minutes=2)])

@socketio.on('send message')
def send_message(data):
    messages.append({'username': users[request.sid], 'message': data['message'], 'timestamp': datetime.now()})
    emit('receive message', {'username': users[request.sid], 'message': data['message']}, broadcast=True)

@socketio.on('update nickname')
def update_nickname(data):
    users[request.sid] = data['nickname']

if __name__ == '__main__':
    socketio.run(app)