from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital_occupancy.db'
db = SQLAlchemy(app)

class OccupancyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    hospital_id = db.Column(db.Integer, nullable=False)
    ping_count = db.Column(db.Integer, nullable=False)
    occupancy_level = db.Column(db.Float, nullable=False)

class CriticalAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient = db.Column(db.String(100), nullable=False)
    bed = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    time = db.Column(db.DateTime, nullable=False)

@app.route('/')
def index():
    total_beds = 125
    beds_available = 25
    critical_alerts = CriticalAlert.query.all()
    
    bed_overview = {
        'total_beds': total_beds,
        'beds_available': beds_available,
        'critical_alerts_count': len(critical_alerts)
    }
    
    return render_template('index.html', bed_overview=bed_overview, critical_alerts=critical_alerts)

if __name__ == '__main__':
    app.run(debug=True)