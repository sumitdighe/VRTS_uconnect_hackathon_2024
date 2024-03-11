import csv
import os
import time
import psutil as ps
from sklearn.preprocessing import LabelEncoder

flag = False  # flag for permission

def get_logged_in_users():
    users = ps.users()
    guest_users = 0
    host_users = 0
    for user in users:
        if user.terminal == '':
            guest_users += 1
        else:
            host_users += 1
    return guest_users, host_users


def get_destination_host_count():
    connections = ps.net_connections(kind='tcp')
    remote_addrs = set()
    for connection in connections:
        if connection.status == ps.CONN_ESTABLISHED:
            remote_addrs.add(connection.raddr[0])
    return len(remote_addrs)


def get_disk_metrics():
    net_io = ps.net_io_counters()
    gln, hln = get_logged_in_users()
    return {
        'src_bytes': net_io.bytes_sent,
        'dst_bytes': net_io.bytes_recv,
        'logged_in': gln or hln,  # CHECKKKKKK
        'is_guest_login': gln,
        'is_host_login': hln,
        'dst_host_count': get_destination_host_count()

    }


def append_to_csv(filename, data):
    with open(filename, mode='a', newline='\n') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            # Write header only if the file is empty
            writer.writeheader()
        writer.writerow(data)
        file.flush()
        os.fsync(file.fileno())

    file.close()


# Network model ML
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score

# Assuming your dataset is in a DataFrame named 'df'
df = pd.read_csv('NetworkData.csv')

# Selecting the columns of interest
#selected_columns = ['src_bytes', 'dst_bytes', 'logged_in', 'is_guest_login', 'is_host_login', 'dst_host_count', 'class']
df_selected = df

# Split the dataset into features (X) and target variable (y)
y = df_selected['class']
X = df_selected.drop('class', axis=1)


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create individual classifiers
gbc = GradientBoostingClassifier()
abc = AdaBoostClassifier()
rfc = RandomForestClassifier()

# Create a voting classifier
voting_classifier = VotingClassifier(estimators=[
    ('gbc', gbc),
    ('abc', abc),
    ('rfc', rfc)
], voting='soft')  # You can use 'soft' voting as well if classifiers provide probabilities

# Train the voting classifier
voting_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = voting_classifier.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# ----------------------------final prediction

# nw_data = pd.read_csv('realdataset2.csv', usecols=['src_bytes', 'dst_bytes', 'logged_in', 'is_guest_login', 'is_host_login', 'dst_host_count', 'class'])
#
# x_real_test = nw_data.drop('class', axis=1)
# y_real_pred = clf.predict(x_real_test)
# print(y_real_pred)


# ------------------------------------

# Specify the CSV file name
csv_filename = 'realdataset2.csv'

# Run the loop continuously
count = 1
while True:

    while count <= 10:
        disk_metrics_data = get_disk_metrics()
        # print(f"Data: {disk_metrics_data}")
        append_to_csv(csv_filename, disk_metrics_data)
        time.sleep(1)  # Adjust the sleep duration as needed
        count += 1

    from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, RandomForestClassifier, \
        VotingClassifier

    print("logs collected")
    # Load the test dataset into a DataFrame
    df_test = pd.read_csv('realdataset2.csv')

    # Selecting the columns of interest used during training
    selected_columns = ['src_bytes', 'dst_bytes', 'logged_in', 'is_guest_login', 'is_host_login', 'dst_host_count']

    # Assuming your model and other relevant code are already defined (as shown in the previous examples)

    # Select the same columns in the test set as used during training
    X_test_data = df_test[selected_columns]

    # Make predictions on the test set using the trained voting classifier
    predictions = voting_classifier.predict(X_test_data)

    # Append the predictions to the test DataFrame
    df_test['predicted_class'] = predictions

    df_test.to_csv("created.csv")


    def append_csv(source_file, destination_file):
        # Read the contents of the source CSV file
        with open(source_file, 'r', newline='') as source_csv:
            source_reader = csv.reader(source_csv)
            data_to_append = [row[1:] for row in list(source_reader)[1:]]

        # Append the contents to the destination CSV file
        with open(destination_file, 'a', newline='') as destination_csv:
            destination_writer = csv.writer(destination_csv)
            destination_writer.writerows(data_to_append)


    # Replace 'source.csv' and 'destination.csv' with your file names
    source_file = 'created.csv'
    destination_file = 'NetworkData.csv'

    # Call the function to append contents
    append_csv(source_file, destination_file)

    print(f"Contents of '{source_file}' appended to '{destination_file}' successfully.")

    # Display the DataFrame with the predicted values
    print(df_test['predicted_class'])
    is_anomaly_present = False
    for i in df_test['predicted_class']:
        if i != 'normal':
            is_anomaly_present = True

    if is_anomaly_present:
        command = 'python Gui.py'
        os.system(command)

    count = 1
    with open(csv_filename, mode='w', newline='\n') as file:
        file.close()

# give to model

# ui s----------

