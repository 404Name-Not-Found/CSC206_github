from flask import Flask, render_template
import home as Home
import page1 as Page1
import display as Display

app = Flask(__name__)

cars = [
    {
        "id": 1,
        "Make": "Toyota",
        "Model": "4-Runner",
        "Year": "2013",
        "Color": "White"
    },
    {
        "id": 2,
        "Make": "Honda",
        "Model": "Civic",
        "Year": "2020",
        "Color": "Blue"
    },
    {
        "id": 3,
        "Make": "Ford",
        "Model": "F-150",
        "Year": "2018",
        "Color": "Red"
    },
    {
        "id": 4,
        "Make": "Chevrolet",
        "Model": "Tahoe",
        "Year": "2022",
        "Color": "Black"
    }
]


@app.route('/')
@app.route('/home')
def home():
    content = Display.display.render(
        all_cars=cars
    )
    html = Home.header.render(
        content=content
    )
    return html


@app.route('/page1')
def show_page1():
    html = Page1.header.render()
    return html


if __name__ == '__main__':
    app.run(debug=True)
