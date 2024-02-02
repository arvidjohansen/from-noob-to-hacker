from flask import Flask, render_template_string, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('game.html')
    return render_template_string('''
    <html>
        <head>
            <script src="https://unpkg.com/htmx.org@1.6.1"></script>
        </head>
        <body>
            {% for _ in range(10) %}
                <div style="display: flex;">
                    {% for _ in range(10) %}
                        <div hx-get="/color" hx-trigger="every 1s" style="width: 20px; height: 20px;"></div>
                    {% endfor %}
                </div>
            {% endfor %}
        </body>
    </html>
    ''')
"""
@app.route('/color')
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'background-color: rgb({r},{g},{b});', 200, {'Content-Type': 'text/css'}
"""
@app.route('/color')
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # return f'<div class="'
    return f'<div  hx-get="/color" hx-trigger="every 1s" hx-swap="outerHTML" class="col-md-1 m-1" style="background-color: rgb({r},{g},{b});"></div>'
    return f'<div  class="col-md-1" style="background-color: rgb({r},{g},{b});"></div>'
    return f'<div hx-get="/color" hx-trigger="every 1s" hx-swap="outerHTML" class="m-1" style="width: 20px; height: 20px; background-color: rgb({r},{g},{b});"></div>'



if __name__ == "__main__":
    app.run(debug=True)