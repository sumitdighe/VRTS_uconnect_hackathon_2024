# Anomaly Detection System for Database Activity Logs

This project is a web-based anomaly detection system for monitoring database activity logs. It utilizes machine learning techniques to detect anomalies in the database activity.

## Features

- **Data Collection:** Captures database activity logs, including queries, transactions, and system events.
- **Feature Engineering:** Extracts relevant features such as query frequency, data access patterns, and transaction volume.
- **Model Training:** Utilizes machine learning algorithms (e.g., Isolation Forest) to train the anomaly detection model.
- **Real-time Monitoring:** Continuously monitors database activities and compares them against learned patterns.
- **Alerting Mechanism:** Triggers alerts and notifications for detected anomalies, including severity levels and recommended actions.
- **Adaptive Learning:** Incorporates feedback loops to adapt the model to evolving database environments and usage patterns.

## Installation

```bash
# Clone this repository using the following command:
git clone <repository_url>

# Navigate to the project directory:
cd <repository_name>

# Install the required dependencies:
pip install -r requirements.txt
```

## Usage
```bash
# Run the Flask application by executing:
python app.py
```
Access the application in your web browser at http://localhost:5000.

Enter the timestamp and value for new data points to be added.

View the plotted data points to monitor anomalies.


--------------------------------------------


### This README.md provides instructions on installation, usage, and the features of the anomaly detection system with included bash scripts.
