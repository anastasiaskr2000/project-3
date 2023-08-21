from flask import Flask, jsonify,render_template,send_file
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from flask_cors import CORS
import sqlite3
import json,os

app = Flask(__name__)
CORS(app)

Base = declarative_base()

class CrimeData(Base):
    __tablename__ = 'crime_data'
    
    id = Column(Integer, primary_key=True)  
    X = Column(String)
    Y = Column(String)
    OBJECTID = Column(Integer)  
    EVENT_UNIQUE_ID = Column(String)
    REPORT_DATE = Column(Date)
    OCC_DATE = Column(Date)
    OCC_YEAR = Column(Integer)
    OCC_MONTH = Column(Integer)
    OCC_HOUR = Column(Integer)
    DIVISION = Column(String)
    LOCATION_TYPE = Column(String)
    PREMISES_TYPE = Column(String)
    OFFENCE = Column(String)
    MCI_CATEGORY = Column(String)
    HOOD_158 = Column(Integer)
    NEIGHBOURHOOD_158 = Column(String)
    HOOD_140 = Column(Integer)
    NEIGHBOURHOOD_140 = Column(String)


engine = create_engine('sqlite:///crime_data.db') 
Session = sessionmaker(bind=engine)

@app.route('/get_crime_data', methods=['GET'])
def get_crime_data():
    session = Session()
    crime_data = session.query(CrimeData).all() 
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

@app.route('/')
def index():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/crime_chart_data<br/>"
        f"/crime_geojson_data<br/>"
        f"/geojson_data<br/>"
        
    )


   # return render_template('index.html')

@app.route('/crime_chart_data', methods=['GET'])
def crime_chart_data():
    conn = sqlite3.connect('crime_data.db')
    query = """
    SELECT OFFENCE, COUNT(*) as crime_count
    FROM crime_data
    WHERE OCC_YEAR = 2018 AND OFFENCE IN ('Assault', 'Auto Theft', 'Break and Enter', 'Robbery', 'Theft Over')
    GROUP BY OFFENCE;
    """
    cursor = conn.execute(query)
    data = cursor.fetchall()
    conn.close()

    chart_data = [{'crime_type': row[0], 'crime_count': row[1]} for row in data]
    
    return jsonify(chart_data)

@app.route('/crime_geojson_data')
def serve_geojson():
        with open('./project-3/static/js/Major_Crime.geojson','r') as file:
            data = json.load(file)
        return jsonify(data)

@app.route('/geojson_data')
def serve2_geojson():
        with open('./project-3/static/js/toronto_crs84.geojson', 'r') as file:
            data2 = json.load(file)
        return jsonify(data2)

if __name__ == '__main__':
    app.run(debug=True)

