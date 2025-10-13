from flask import Flask, render_template_string
import home as Home
import page1 as Page1

app = Flask(__name__)


# Routes to the home page / starting page
@app.route('/')
@app.route('/home')
def home():
    html = Home.header + Home.content + Home.footer
    return render_template_string(html)


# Routes to the second / login page
@app.route('/page1')
def show_page1():
    html = Page1.header + Page1.footer
    return render_template_string(html)


if __name__ == '__main__':
    app.run()
