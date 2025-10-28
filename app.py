from flask import Flask, render_template
from database import Database

app = Flask(__name__, static_url_path='/static', template_folder='templates')

db = Database(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('display.html')


@app.route('/login')
def show_page1():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
