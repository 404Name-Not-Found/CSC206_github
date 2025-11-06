from flask import Flask, render_template
from database import MyDatabase
from sql import cars
from dotenv import load_dotenv
from decimal import Decimal

load_dotenv()

app = Flask(__name__, static_url_path='/static', template_folder='templates')

db = MyDatabase(app)


# Function that returns all the SQL queries
def sql_queries():

    vSQL = cars.vehicleSQL()


    # To loop through sql queries:
    # https://stackoverflow.com/questions/16947276/flask-sqlalchemy-iterate-column-values-on-a-single-row
    queries = {
        'vehicles': vSQL.all_vehicles(),
        'manufacturer': vSQL.vehicle_names(),
        'vehicle_types': vSQL.vehicle_type(),
        'vehicle_models': vSQL.vehicle_model(),
        'fuel_types': vSQL.vehicle_fuel_type(),
        'colors': vSQL.colors(),
    }

    all_cars = {}

    for key, sql in queries.items():
        all_cars[key] = db.query(sql)

    return all_cars


@app.route('/')
@app.route('/home')
def home():

    car_query = sql_queries()

    qSQL = cars.vehicleSQL()
    output = db.query(qSQL.sellable_vehicles())

    return render_template('display.html', cars=car_query, vehicles=output, include_filters=True)


@app.route('/vehicle_type/<vehicle_type_name>')
def vehicle_details(vehicle_type_name):

    car_query = sql_queries()

    vSQL = cars.vehicleSQL()
    output = db.query(vSQL.vehicle_by_type(vehicle_type_name))

    return render_template('results.html', vehicles=output, cars=car_query)


@app.route('/manufacturers/<manufacturer_name>')
def manufacturer(manufacturer_name):

    car_query = sql_queries()

    qSQL = cars.vehicleSQL()
    output = db.query(qSQL.vehicles_by_manufacturer(manufacturer_name))

    return render_template('results.html', vehicles=output, cars=car_query, display_color=True)

@app.route('/model_name/<model_name>')
def model(model_name):

    car_query = sql_queries()

    qSQL = cars.vehicleSQL()
    output = db.query(qSQL.vehicle_by_model(model_name))

    return render_template('results.html', vehicles=output, cars=car_query)

@app.route('/fuel_type/<fuel>')
def fuels(fuel):

    car_query = sql_queries()

    qSQL = cars.vehicleSQL()
    output = db.query(qSQL.vehicle_by_fuel(fuel))

    return render_template('results.html', vehicles=output, cars=car_query)

@app.route('/colors/<color>')
def colors(color):

    car_query = sql_queries()

    qSQL = cars.vehicleSQL()
    output = db.query(qSQL.vehicle_by_color(color))

    return render_template('results.html', vehicles=output, cars=car_query)


@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html', cars={})


@app.route('/sales')
def sales():

    qSQL = cars.vehicleSQL()
    output = db.query(qSQL.sale())

    return render_template('reports.html', info=output)


@app.route('/seller')
def seller():

    qSQL = cars.vehicleSQL()
    output = db.query(qSQL.seller())

    return render_template('seller.html', info=output)


@app.route('/statistics')
def stats():

    qSQL = cars.vehicleSQL()
    output = db.query(qSQL.statistics())

    return render_template('statistics.html', info=output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
