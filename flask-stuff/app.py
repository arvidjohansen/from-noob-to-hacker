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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///downloads.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config["DOWNLOAD_FOLDER"] = "downloads"
db = SQLAlchemy(app)
app.jinja_env.filters['time_since'] = time_since
app.jinja_env.filters['default_if_none'] = default_if_none

class Status(Enum):
    PRE_DOWNLOAD = "pre_download"
    DOWNLOADING = "downloading"
    FINISHED = "finished"
    error = "error"
    ERROR = "error"
    

    @property
    def full_name(self):
        if self == Status.PRE_DOWNLOAD:
            return "Not started"
        elif self == Status.DOWNLOADING:
            return "Downloading"
        elif self == Status.FINISHED:
            return "Finished"
        elif self == Status.ERROR:
            return "Error"
        elif self == Status.error:
            return "Error"
    


class Downloader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    edited_at = db.Column(db.DateTime, onupdate=func.now())
    status = db.Column(db.Enum(Status), default=Status.PRE_DOWNLOAD)

    def download(self):
        from pdb import set_trace;set_trace()
        try:
            youtube = YouTube(self.url)
            video = youtube.streams.get_highest_resolution()
            video.download(app.config['DOWNLOAD_FOLDER'])
            self.status = 'FINISHED'
            db.session.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.status = 'ERROR'
            db.session.commit()

    @property
    def get_status_name(self):
        return self.status.full_name

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

@app.route('/download/<int:id>', methods=['POST'])
def download(id):
    downloader = Downloader.query.get_or_404(id)
    downloader.download()
    return redirect(url_for('home'))

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
        https://flask-migrate.readthedocs.io/en/latest/
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
        
