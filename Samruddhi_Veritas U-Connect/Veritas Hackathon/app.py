# Import necessary libraries
import pandas as pd
from sklearn.ensemble import IsolationForest
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask application
app = Flask(__name__)

# Set up SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anomaly_detection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(20))
    value = db.Column(db.Float)
    anomaly = db.Column(db.Integer)  # 1 for normal, -1 for anomaly

    def __repr__(self):
        return f'<Data {self.timestamp} - {self.value} - {self.anomaly}>'

# Define routes and views for Flask application
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        timestamp = request.form['timestamp']
        value = float(request.form['value'])

        # Create a new Data object and add it to the database
        new_data = Data(timestamp=timestamp, value=value)
        db.session.add(new_data)
        db.session.commit()

        return redirect(url_for('plot'))

    return render_template('index.html')

@app.route('/plot')
def plot():
    # Load all data points
    data_points = Data.query.all()
    
    # Prepare data for visualization
    points = [{'timestamp': dp.timestamp, 'value': dp.value, 'anomaly': dp.anomaly} for dp in data_points]

    return render_template('plot.html', points=points)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
