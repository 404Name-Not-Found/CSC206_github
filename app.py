from flask import Flask, render_template, request
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
        'vehicle_years': vSQL.vehicle_years(),
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

    # Filter help from my boi as well
    manID = request.args.get('manufacturer_name')
    vehicletypeID = request.args.get('vehicle_type')
    modelyear = request.args.get('model_year')
    fueltype = request.args.get('fuel_type')
    colorid = request.args.get('color_selection')

    filters = {}
    try:
        if manID:
            filters['manID'] = int(manID)
    except ValueError:
        pass
    try:
        if vehicletypeID:
            filters['vehicletypeID'] = int(vehicletypeID)
    except ValueError:
        pass
    try:
        if modelyear:
            filters['model_year'] = modelyear
    except ValueError:
        pass
    if fueltype:
        filters['fueltype'] = fueltype
    try:
        if colorid:
            filters['colorid'] = int(colorid)
    except ValueError:
        pass

    qSQL = cars.vehicleSQL()

    car_query = sql_queries()
    output = db.query(qSQL.sellable_vehicles(filters if filter else None))

    return render_template('display.html', cars=car_query, vehicles=output, include_filters=True, display_color=True)


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
