import sys


import PySimpleGUI as sg
import csv
import os
import time
import psutil as ps

flag = False  # flag for permission

# ui-s
layout = [
    [sg.Text('Permission Settings')],
    [sg.Checkbox('Accept permission', key='-EXECUTE-', default=False)],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

window = sg.Window('Permission Manager', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    if event == 'Submit':
        permission_info = {
            'Execute': values['-EXECUTE-']
        }

        if all(permission_info.values()):
            print("Okay")
            flag = True
            break
        else:
            print("Permission not granted. Program terminated.")
            sys.exit(0)

window.close()


# ui-e
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
    """
    Count the number of unique remote addresses for active TCP connections.

    :return: The count of unique remote addresses
    """
    connections = ps.net_connections(kind='tcp')
    remote_addrs = set()
    for connection in connections:
        if connection.status == ps.CONN_ESTABLISHED:
            remote_addrs.add(connection.raddr[0])
    return len(remote_addrs)
def get_disk_metrics():
    print("hi")
    disk_io = ps.disk_io_counters()
    cpu = ps.Process()
    net_io = ps.net_io_counters()
    gln, hln = get_logged_in_users()
    return {
        # 'read_count': disk_io.read_count,
        # 'write_count': disk_io.write_count,
        # 'src_bytes': disk_io.read_bytes, #read
        # 'dst_bytes': disk_io.write_bytes, #write
        # 'read_time': disk_io.read_time,
        # 'write_time': disk_io.write_time,
        # 'ctx_switches': cpu.num_ctx_switches(),
        # 'cpu_percent': cpu.cpu_percent(),
        'src_bytes': net_io.bytes_sent,
        'dst_bytes': net_io.bytes_recv,
        # 'packets_sent': net_io.packets_sent,
        # 'packets_recv': net_io.packets_recv,
        # 'err_on_in': net_io.errin,
        # 'err_on_out': net_io.errout,
        # 'dropin': net_io.dropin,
        # 'dropout': net_io.dropout,
        # 'system_exception_dispatches': ps.cpu_times().interrupt,
        'logged_in':gln+hln,              # CHECKKKKKK
        'is_guest_login':gln,
        'is_host_login':hln,
        'dst_host_count': get_destination_host_count()

    }

# def get_cpu_metrics:
#     return {
#         'hour': time.strftime('%Y-%m-%d %H:%M:%S'),
#         'cpu': ps.cpu_percent()
#     }


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
df = pd.read_csv('Train_data.csv')
# Selecting the columns of interest
selected_columns = ['src_bytes', 'dst_bytes', 'logged_in', 'is_guest_login', 'is_host_login', 'dst_host_count', 'class']
df_selected = df[selected_columns]

# Split the dataset into features (X) and target variable (y)
X = df_selected.drop('class', axis=1)
y = df_selected['class']

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

    # Display the DataFrame with the predicted values
    print(df_test['predicted_class'])
    is_anomaly_present = False
    for i in df_test['predicted_class']:
        if i!='normal':
            is_anomaly_present = True

    if is_anomaly_present:
        popup = [
            [sg.Text('Anomaly detected!')],
            [sg.Text('Warning: An anomaly has been detected in the system. Please take appropriate action.')],
            [sg.Button('OK')]
        ]

        popup_window = sg.Window('Anomaly Detected', popup)

        # while anomaly:
        event, values = popup_window.read()
        if event == sg.WIN_CLOSED or event == 'OK':
        # break

            popup_window.close()

    # -----------------
    count=1
    with open(csv_filename, mode='w', newline='\n') as file:
        file.close()



# give to model


# ui s----------

