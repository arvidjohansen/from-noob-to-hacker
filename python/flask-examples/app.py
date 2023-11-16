"""
A simple web application.
"""
# WARNING START: do not change the following two lines of code.
from flask import Flask, render_template

app = Flask(__name__)
# WARNING END: do not change the previous two lines of code.


CONTEXT = {
    "title":"Velkommen til Arvids hjemmeside",
    }

data = [{'firstName': 'Petter', 'lastName': 'Gravlaks', 'title': 'Markedsarbeider', 'age': 57}, {'firstName': 'Arvid', 'lastName': 'Skjelberg', 'title': 'Sjef', 'age': 72}, {'firstName': 'Arvid', 'lastName': 'Gravlaks', 'title': 'Markedsarbeider', 'age': 36}, {'firstName': 'Petter', 'lastName': 'Gravlaks', 'title': 'Sjef', 'age': 60}, {'firstName': 'Petter', 'lastName': 'Tennisen', 'title': 'Sjef', 'age': 30}, {'firstName': 'Jonathan', 'lastName': 'Gravlaks', 'title': 'Markedsarbeider', 'age': 51}, {'firstName': 'Petter', 'lastName': 'Tennisen', 'title': 'Sjef', 'age': 60}, {'firstName': 'Jonas', 'lastName': 'Gravlaks', 'title': 'Sjef', 'age': 48}, {'firstName': 'Jonathan', 'lastName': 'Skjelberg', 'title': 'Kontoransatt', 'age': 77}, {'firstName': 'Petter', 'lastName': 'Skjelberg', 'title': 'Sjef', 'age': 48}]



@app.route("/")
def home():
    context = CONTEXT.copy()
    context
    return render_template("home.html",active_page="home")

@app.route("/about-us")
def about_us():
    return render_template("about-us.html", active_page="about-us", data=data)


app.run(
    debug=True,
)