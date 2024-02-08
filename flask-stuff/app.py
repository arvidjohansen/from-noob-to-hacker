# app.py

import sys
from flask import Flask, render_template, redirect, request
from flask import flash, get_flashed_messages
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.sql import func
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from utilities import time_since, default_if_none

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///downloads.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
app.jinja_env.filters['time_since'] = time_since
app.jinja_env.filters['default_if_none'] = default_if_none


class Downloader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    edited_at = db.Column(db.DateTime, onupdate=func.now())
class DownloadForm(FlaskForm):
    urls = TextAreaField('URLs', validators=[DataRequired()])

@app.route('/home')
def home():
    return redirect(url_for('index'))
@app.route('/')
def index():
    form = DownloadForm()
    downloads = Downloader.query.filter().order_by(Downloader.created_at.desc())
    return render_template('index.html', 
                           form=form, 
                           object_list=downloads)

@app.route('/submit', methods=['POST'])
def submit():
    form = DownloadForm()
    if form.validate_on_submit():
        urls = form.urls.data.split('\n')
        for url in urls:
            if url.strip():
                downloader = Downloader(url=url.strip())
                db.session.add(downloader)
        db.session.commit()
        flash('Download URLs submitted successfully.')
        return redirect(url_for('index'))
    else:
        flash('Invalid data submitted.')
    return render_template('index.html', form=form)

@app.route('/downloads')
def downloads():
    all_downloads = Downloader.query.all()
    return render_template('downloads.html', all_downloads=all_downloads)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    downloader = Downloader.query.get_or_404(id)
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            return render_template('edit.html', downloader=downloader, error="URL cannot be empty")
        downloader.url = url
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', downloader=downloader)

@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    downloader = Downloader.query.get_or_404(id)
    db.session.delete(downloader)
    db.session.commit()
    flash('Downloader successfully deleted.')
    return redirect(url_for('downloads'))


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
        """
        In case of future changes to DB schema, you can use the following code 
        to add new columns to the existing table.
        Instead of using Migrate App.
        
        import sqlite3
        # Connect to your SQLite database
        conn = sqlite3.connect('/path/to/your/database.db')
        # Create a cursor object
        c = conn.cursor()
        # Execute raw SQL commands to add the columns
        c.execute("ALTER TABLE downloader ADD COLUMN created_at DATETIME DEFAULT CURRENT_TIMESTAMP;")
        c.execute("ALTER TABLE downloader ADD COLUMN edited_at DATETIME;")
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        """
        
