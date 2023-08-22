from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

engine = create_engine('sqlite:///static/data/crime_data.db') 
Session = sessionmaker(bind=engine)

database_path2 = 'sqlite:///static/data/crime_count.db'
engine2 = create_engine(database_path2)
Session2 = sessionmaker(bind=engine2)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes for the Toronto Crime Data:<br/><br>"
        f"-- Crime Data for loading the dashboard: <a href=\"/get_crime_data\">/get_crime_data<a><br/>"
        f"-- : <a href=\"/crime_chart_data\">/crime_chart_data<a><br/>"
        f"-- : <a href=\"/crime_geojson_data\">/crime_geojson_data<a><br/>"
        f"-- : <a href=\"/homicide_data\">/homicide_data<a><br/>"
        f"NOTE: If no end-date is provided, the trip api calculates stats through 08/23/17<br>" 
    )

@app.route('/get_crime_data/', methods=['GET'])
def get_crime_data():
    session = Session()
    sql_q = text("SELECT * FROM crime_data")
    crime_data = session.execute(sql_q).all() 
    session.close()

    # Convert crime_data to a list of dictionaries
    crime_data_dict_list = [
        {
            'id': item.id,
            'X': item.X,
            'Y': item.Y,
            'OBJECTID': item.OBJECTID,  # Correct typo
            'EVENT_UNIQUE_ID': item.EVENT_UNIQUE_ID,
            'REPORT_DATE': item.REPORT_DATE,
            'OCC_DATE': item.OCC_DATE,
            'OCC_YEAR': item.OCC_YEAR,
            'OCC_MONTH': item.OCC_MONTH,
            'OCC_HOUR': item.OCC_HOUR,
            'DIVISION': item.DIVISION,
            'LOCATION_TYPE': item.LOCATION_TYPE,
            'PREMISES_TYPE': item.PREMISES_TYPE,
            'OFFENCE': item.OFFENCE,
            'MCI_CATEGORY': item.MCI_CATEGORY,
            'HOOD_158': item.HOOD_158,
            'NEIGHBOURHOOD_158': item.NEIGHBOURHOOD_158,
            'HOOD_140': item.HOOD_140,
            'NEIGHBOURHOOD_140': item.NEIGHBOURHOOD_140
        }
        for item in crime_data
    ]
    return jsonify(crime_data_dict_list)

@app.route('/crime_chart_data',methods = ['GET'])
def get_crime_chart():
    session2 = Session2()
    sql_query = text("SELECT * FROM crime_count;")
    crime_counts = session2.execute(sql_query).all()
    session2.close()

    # Convert the data to a list of dictionaries
    crime_data = []
    for count in crime_counts:
        crime_data.append({
            'Id': count.Id,
            'Year': count.Year,
            'Month': count.Month,
            'Assault': count.Assault,
            'Auto_Theft': count.Auto_Theft,
            'Break_and_Enter': count.Break_and_Enter,
            'Robbery': count.Robbery,
            'Theft_Over': count.Theft_Over
        })

    return jsonify(crime_data)

@app.route('/homicide_data',methods=['GET'])
def homicide():
    with open('static/data/Homocide_data.json','r') as hfile:
            homicide_data = json.load(hfile)
    return jsonify(homicide_data)

@app.route('/crime_geojson_data')
def serve_geojson():
        with open('static/data/Major_Crime.geojson','r') as file:
            data = json.load(file)
        return jsonify(data)

@app.route('/geojson_data')
def serve2_geojson():
        with open('static/data/toronto_crs84.geojson', 'r') as geo1_file:
            data2 = json.load(geo1_file)
        return jsonify(data2)

@app.route('/homicide_geojson')
def homicide_geojson_serve():
     with open('static/data/Homicides.geojson','r') as geo2_file:
          data3 = json.load(geo2_file)
          return jsonify(data3)

@app.route('/text_data')
def text_data_serve():
     with open('static/data/Modified_major_crime.json','r') as text_file:
          data3 = json.load(text_file)
          return jsonify(data3)

if __name__ == '__main__':
    app.run(debug=True)

