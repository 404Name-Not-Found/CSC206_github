from flask import Flask
import home as Home
import page1 as Page1

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    html = Home.header.render()
    return html


@app.route('/page1')
def show_page1():
    html = Page1.header.render()
    return html


if __name__ == '__main__':
    app.run(debug=True)
