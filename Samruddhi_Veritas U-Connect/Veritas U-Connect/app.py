from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest
import plotly.graph_objs as go

app = Flask(__name__)

# Initialize SQLite database
def initialize_database():
    conn = sqlite3.connect('database_activity.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS activity_logs (
                    id INTEGER PRIMARY KEY,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    query TEXT,
                    user TEXT
                )''')
    conn.commit()
    conn.close()

# Insert activity logs into the database
def insert_activity_log(query, user):
    conn = sqlite3.connect('database_activity.db')
    c = conn.cursor()
    c.execute('''INSERT INTO activity_logs (query, user) 
                 VALUES (?, ?)''', (query, user))
    conn.commit()
    conn.close()

# Train Isolation Forest model
def train_model():
    conn = sqlite3.connect('database_activity.db')
    df = pd.read_sql_query("SELECT * FROM activity_logs", conn)
    conn.close()

    df = pd.get_dummies(df, columns=['query', 'user'])

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(df.drop(columns=['timestamp', 'id']))

    return model

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        user = request.form['user']
        insert_activity_log(query, user)
        return render_template('submit_success.html')
    return render_template('index.html')

# Route for real-time anomaly detection
@app.route('/detect_anomalies', methods=['GET'])
def detect_anomalies():
    model = train_model()
    conn = sqlite3.connect('database_activity.db')
    new_df = pd.read_sql_query("SELECT * FROM activity_logs", conn)
    conn.close()

    new_df = pd.get_dummies(new_df, columns=['query', 'user'])
    new_df['anomaly'] = model.predict(new_df.drop(columns=['timestamp', 'id']))

    anomalies = new_df[new_df['anomaly'] == -1][['timestamp', 'anomaly']]

    # Create an interactive Plotly chart for anomalies
    trace = go.Scatter(x=anomalies['timestamp'], y=anomalies['anomaly'],
                       mode='markers', marker=dict(color='red', size=8),
                       name='Anomalies')
    layout = go.Layout(title='Detected Anomalies',
                       xaxis=dict(title='Timestamp'),
                       yaxis=dict(title='Anomaly'),
                       showlegend=True)
    chart = go.Figure(data=[trace], layout=layout)
    anomalies_chart = chart.to_html(full_html=False)

    return render_template('anomalies.html', anomalies_chart=anomalies_chart)

# Route for real-time updates of anomalies (AJAX request)
@app.route('/get_anomalies', methods=['GET'])
def get_anomalies():
    model = train_model()
    conn = sqlite3.connect('database_activity.db')
    new_df = pd.read_sql_query("SELECT * FROM activity_logs", conn)
    conn.close()

    new_df = pd.get_dummies(new_df, columns=['query', 'user'])
    new_df['anomaly'] = model.predict(new_df.drop(columns=['timestamp', 'id']))

    anomalies = new_df[new_df['anomaly'] == -1][['timestamp', 'anomaly']]

    # Prepare data for JSON response
    data = [{'timestamp': str(timestamp), 'anomaly': anomaly}
            for timestamp, anomaly in zip(anomalies['timestamp'], anomalies['anomaly'])]

    return jsonify(data)

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
