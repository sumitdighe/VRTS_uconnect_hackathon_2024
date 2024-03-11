import csv
import os
import time
import psutil as ps
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM

# Load the existing dataset
data = pd.read_csv('cpu_full.csv')
data = data.dropna()

# Extract timestamp features
data['datetime'] = pd.to_datetime(data['datetime'])
data['hour'] = data['datetime'].dt.hour

# Create a dataframe from the data
df = pd.DataFrame(data, columns=['hour', 'cpu'])

# Initialize Isolation Forest model
isolation_forest_model = IsolationForest(n_estimators=120, contamination=0.005, max_samples=0.5)

# Initialize One-Class SVM model
svm_model = OneClassSVM(nu=0.005)

def get_disk_metrics():
    return {
        'hour': time.strftime('%Y-%m-%d %H:%M:%S'),
        'cpu': ps.cpu_percent()

    }

def append_to_cpucsv(filename, data):
    with open(filename, mode='a', newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            # Write header only if the file is empty
            writer.writeheader()
        writer.writerow(data)
        file.flush()
        os.fsync(file.fileno())

    file.close()

# Specify the CSV file name
csv_filename = 'realdataset3.csv'

# Run the loop continuously
count = 1
while True:
    while count <= 10:
        disk_metrics_data = get_disk_metrics()
        append_to_cpucsv(csv_filename, disk_metrics_data)
        time.sleep(1)  # Adjust the sleep duration as needed
        count += 1

    # Read the real dataset from CSV
    real_cpu_data = pd.read_csv('realdataset3.csv')
    real_cpu_data['datetime'] = pd.to_datetime(data['datetime'])
    real_cpu_data['hour'] = real_cpu_data['datetime'].dt.hour

    df2 = pd.DataFrame(real_cpu_data,columns=['hour', 'cpu'])


    # Fit Isolation Forest model to the data
    isolation_forest_model.fit(df)

    # Predict outliers using Isolation Forest
    isolation_forest_prediction = isolation_forest_model.predict(df2)

    # Fit One-Class SVM model to the data
    svm_model.fit(df)

    # Predict outliers using One-Class SVM
    svm_prediction = svm_model.predict(df2)

    combined_prediction = np.array([isolation_forest_prediction, svm_prediction])

    # Use voting to identify outliers detected by both models
    combined_prediction = np.sum(combined_prediction,axis=0)
    combined_prediction[combined_prediction == -2] = -1
    combined_prediction[combined_prediction > -2] = 1

    # Identify combined outliers
    combined_outliers = np.where(combined_prediction == -1)[0]

    # Plot outliers identified by both models
    plt.scatter(df2['hour'][combined_outliers], df2['cpu'][combined_outliers], color='purple', label='Combined Outliers')
    plt.scatter(df2['hour'][isolation_forest_prediction == -1], df2['cpu'][isolation_forest_prediction == -1],
                color='red', label='Isolation Forest Outliers')
    plt.scatter(df2['hour'][svm_prediction == -1], df2['cpu'][svm_prediction == -1],
                color='orange', label='SVM Outliers')

    plt.title("Data points with outliers identified by Isolation Forest and One-Class SVM")
    plt.legend()
    plt.show()

    # Reset the count for the next iteration
    count = 1
    with open(csv_filename, mode='w', newline='\n') as file:
        file.close()

    print("CPU anomalies: ",combined_prediction)

    for i in combined_prediction:
        if i==-1:
            command = 'python Gui.py'
            os.system(command)
            break
