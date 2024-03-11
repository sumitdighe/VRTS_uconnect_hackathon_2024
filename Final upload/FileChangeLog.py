import os
import time

from sklearn.svm import OneClassSVM
time.sleep(25)
file_change_logs = []

def collect_file_change_logs(root_directory='/', max_files=2000):

    file_count = 0

    for root, dirs, files in os.walk(root_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_change_logs.append({
                'file_path': file_path,
                'timestamp': os.path.getmtime(file_path),  # Using file modification time
                'file_size': os.path.getsize(file_path),
                'file_attributes': os.stat(file_path).st_mode,
                # Add other attributes as needed
            })
            file_count += 1
            if file_count >= max_files:
                return file_change_logs

    return file_change_logs

# Example usage:
file_logs = collect_file_change_logs(root_directory='/', max_files=20000)


from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np

# Assuming 'file_change_logs' contains the file change log data as a list of dictionaries
# Each dictionary represents a file change log with keys: 'timestamp', 'file_size', 'file_attributes'

# Extracting features
features = []
for log in file_change_logs:
    features.append([log['timestamp'], log['file_size'], log['file_attributes']])

# Normalizing features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)




# Fitting the Isolation Forest model
model = IsolationForest(contamination=0.00001)  # Contamination parameter can be adjusted based on the expected proportion of anomalies
model.fit(scaled_features)

# Predicting anomalies
predictions = model.predict(scaled_features)



# Printing anomalies
anomalies = np.where(predictions == -1)[0]

print("Detected anomalies:")
for idx in anomalies:
   if(idx!=-1):
       command = 'python Gui.py'
       os.system(command)
       break
   print(file_change_logs[idx])


