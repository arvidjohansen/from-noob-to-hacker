from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<Note {self.id}>'

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        password = request.form['password']
        if message:
            new_note = Note(message=message)
            if password:
                new_note.set_password(password)
            db.session.add(new_note)
            db.session.commit()
            flash('Note created successfully!')
            return redirect(url_for('view_note', note_id=new_note.id))
        else:
            flash('Message cannot be empty!')
    return render_template('index.html')

@app.route('/note/<int:note_id>', methods=['GET', 'POST'])
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        password_attempt = request.form['password']
        if note.password_hash and not note.check_password(password_attempt):
            flash('Incorrect password!')
        else:
            return render_template('note.html', note=note)
    return render_template('password.html', note_id=note_id)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
