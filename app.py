import streamlit as st
import psutil
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import LocalOutlierFactor
import numpy as np
import json
from streamlit_lottie import st_lottie
import base64
import re
import plotly.graph_objects as go
import time
import datetime
import pytz
from pycaret.anomaly import *

def load_lottiefile(filepath: str):
  with open(filepath, "r") as f:
    return json.load(f)

def get_img_as_base64(file):
  with open(file, "rb") as f:
    data = f.read()
    return base64.b64encode(data).decode()

def calculate_zscore_mad(df, y_col):
  df['z_score'] = (df[y_col] - df[y_col].mean()) / df[y_col].std()
  return df

def apply_isolation_forest_train_test(df, y_col, contamination_iso):
  train_size = 2920
  train_data = df.iloc[:train_size]
  test_data = df.iloc[train_size:]

  iso_forest = IsolationForest(contamination=contamination_iso, random_state=42)

  X_train = train_data[y_col].values.reshape(-1, 1)
  iso_forest.fit(X_train)

  preds_iso_forest = iso_forest.predict(test_data[y_col].values.reshape(-1, 1))

  test_data['anomaly_iforest'] = preds_iso_forest

  df_result = pd.concat([train_data, test_data])
  return df_result

def apply_local_outlier_factor_train_test(df, y_col):
  train_size = 2920
  train_data = df.iloc[:train_size]
  test_data = df.iloc[train_size:]

  contamination_lof = 1 / len(train_data)
  lof = LocalOutlierFactor(n_neighbors=20, contamination=contamination_lof)

  scores_lof = lof.fit_predict(test_data[y_col].values.reshape(-1, 1))

  test_data['score_lof'] = -scores_lof

  lof_threshold = test_data['score_lof'].quantile(0.95)
  test_data['anomaly_lof'] = np.where(test_data['score_lof'] > lof_threshold, -1, 1)

  df_result = pd.concat([train_data, test_data])

  return df_result

def identify_anomalies(df, x_col, y_col, detection_method, contamination_iso):
  if detection_method == 'Z-Score':
    df = calculate_zscore_mad(df, y_col)
    anomalies_df = df[(df['z_score'] > 3) | (df['z_score'] < -3)]
    st.subheader('Anomalies Detected by Z-Score:')
    st.write(f'Total Anomalies (Z-Score): {len(anomalies_df)}')
    df['label'] = np.where(df['z_score'] > 2, 1, 0)

  elif detection_method == 'Isolation Forest':
    df = apply_isolation_forest_train_test(df, y_col, contamination_iso)
    anomalies_df = df[df['anomaly_iforest'] == -1]
    st.subheader('Anomalies Detected by Isolation Forest:')
    st.write(f'Total Anomalies (Isolation Forest): {len(anomalies_df)}')

  elif detection_method == 'Local Outlier Factor':
    df = apply_local_outlier_factor_train_test(df, y_col)
    anomalies_df = df[df['anomaly_lof'] == -1]
    st.subheader('Anomalies Detected by Local Outlier Factor:')
    st.write(f'Total Anomalies (Local Outlier Factor): {len(anomalies_df)}')

  fig = px.line(df, x=x_col, y=y_col, title=f'{y_col} with Anomalies')
  fig.update_layout(
    xaxis=dict(title=x_col),
    yaxis=dict(title=y_col),
    hovermode="x unified"
  )

  if not anomalies_df.empty:
    anomaly_threshold = df[y_col].quantile(0.99)
    fig.add_trace(px.scatter(anomalies_df, x=x_col, y=y_col, color_discrete_sequence=['red']).data[0])
    fig.add_shape(
      type='line',
      x0=df[x_col].min(),
      x1=df[x_col].max(),
      y0=anomaly_threshold,
      y1=anomaly_threshold,
      line=dict(color='red', dash='dash'),
    )
    st.write(f'Anomaly Threshold: {anomaly_threshold:.2f}')

    st.subheader('Data Values for Detected Anomalies:')
    st.write(anomalies_df)

    st.plotly_chart(fig)

  if detection_method == 'Z-Score':
    cm = confusion_matrix(df['label'], np.where(df['z_score'] > 3, 1, 0))
    st.subheader('Confusion Matrix for Z-Score:')
    st.table(pd.DataFrame(cm, columns=['Predicted Normal', 'Predicted Anomaly'], index=['Actual Normal', 'Actual Anomaly']))

  elif detection_method == 'Isolation Forest':
    df = apply_isolation_forest_train_test(df, y_col, contamination_iso)

    # Create a binary column for actual anomalies based on is_anomaly and -1 label
    df['actual_anomaly'] = np.where((df['is_anomaly'] == -1) | (df['anomaly_iforest'] == -1), 1, 0)

    # Create a binary column for predicted anomalies based on anomaly_iforest
    df['predicted_anomaly'] = np.where(df['anomaly_iforest'] == -1, 1, 0)

    # Confusion matrix
    cm = confusion_matrix(df['actual_anomaly'], df['predicted_anomaly'], labels=[1, 0])
    st.subheader('Confusion Matrix for Isolation Forest:')
    st.table(pd.DataFrame(cm, columns=['Predicted Anomaly', 'Predicted Normal'], index=['Actual Anomaly', 'Actual Normal']))

  elif detection_method == 'Local Outlier Factor':
    df['actual_anomaly'] = np.where((df['is_anomaly'] == -1) | (df['anomaly_lof'] == -1), 1, 0)
    df['predicted_anomaly'] = np.where(df['anomaly_lof'] == -1, 1, 0)

    cm = confusion_matrix(df['actual_anomaly'], df['predicted_anomaly'], labels=[1, 0])
    st.subheader('Confusion Matrix for Local Outlier Factor:')

    # Display confusion matrix
    st.table(pd.DataFrame(cm, columns=['Predicted Anomaly', 'Predicted Normal'], index=['Actual Anomaly', 'Actual Normal']))

  st.subheader('Distribution of Inliers and Outliers:')
  labels = ['Normal (Inliers)', 'Anomalous (Outliers)']

  if detection_method == 'Z-Score':
    values = [len(df[df['label'] == 0]), len(df[df['label'] == 1])]
  elif detection_method == 'Isolation Forest':
    values = [len(df[df['anomaly_iforest'] == 1]), len(df[df['anomaly_iforest'] == -1])]
  elif detection_method == 'Local Outlier Factor':
    values = [len(df[df['anomaly_lof'] == 1]), len(df[df['anomaly_lof'] == -1])]

  colors = ['green', 'yellow']
  fig_pie = px.pie(names=labels, values=values, title='Inliers and Outliers Distribution', color=labels, color_discrete_map={'Normal (Inliers)': 'green', 'Anomalous (Outliers)': 'yellow'})
  st.plotly_chart(fig_pie)

def main():
    st.set_page_config(page_title="Anomaly Detection System", layout="wide")
    st.title("AI Powered Anomaly Detection System")

    animation_state = "loading"

    lottie_coding = load_lottiefile("/content/coding2.json")

    def display_animation():
        st_lottie(
            lottie_coding,
            speed=0.02,
            reverse=False,
            loop=True,
            quality="low",
            height=None,
            width=None,
            key="anomaly_detection_animation",
        )

    with st.sidebar:
        st.title("Anomaly Detection System")
        choice = st.selectbox(
            "Select Data Type", ["-------","Log File Data", "Realtime Data", "CSV Data"]
        )

    # Display animation while loading
    if animation_state == "loading" and st.session_state.get("animation_state", None) != "stopped":
      display_animation()

    # Stop the animation if a choice is made
    if choice:
        animation_state = "stopped"
        st.session_state.animation_state = "stopped"

    if choice == "CSV Data":
        animation_state = "stopped"

        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
            except pd.errors.EmptyDataError:
                st.error("Uploaded file is empty. Please choose a valid CSV file.")
                return

            st.subheader('Uploaded Dataset:')
            st.write(df.head())

            if df.empty:
                st.warning("No data to analyze. Please choose a different file.")
                return

            x_col = st.selectbox('Select X-axis column:', df.columns)
            y_col = st.selectbox('Select Y-axis column (CPU Utilization):', df.columns)
            detection_method = st.selectbox('Select Anomaly Detection Method:', ['Z-Score', 'Isolation Forest', 'Local Outlier Factor'])

            if detection_method == 'Isolation Forest' or detection_method == 'Local Outlier Factor':
                initial_contamination = 1 / len(df)
                contamination = st.slider('Select Contamination Value', 0.0002, 0.5, initial_contamination, step=0.0001)
            else:
                contamination = 0

            timestamp_column = None
            for column in df.columns:
                if df[column].dtype == 'object' and pd.to_datetime(df[column], errors='coerce').notnull().all():
                    timestamp_column = column
                    break

            if timestamp_column is not None:
                df['is_anomaly'] = 1
                anomalies_timestamp = ["2014-02-19 00:22:00", "2014-02-24 18:37:00", "2014-02-16 00:47:00", "2014-02-23 14:27:00"]
                for each in anomalies_timestamp:
                    df.loc[df[timestamp_column] == each, 'is_anomaly'] = -1

            else:
                st.error("No suitable timestamp column found. Please check your data.")
                return

            df['label'] = 0

            identify_anomalies(df, x_col, y_col, detection_method, contamination)

    elif choice == "Log File Data":
        uploaded_file = st.file_uploader("Upload log file", type=["log"])
        animation_state = "stopped"
        main_logfile_anomaly_detection(uploaded_file)
        
    elif choice == "Realtime Data":
        animation_state = "stopped"
        main_realtime_anomaly_detection()

def get_system_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return cpu_usage, memory_usage, disk_usage

def main_realtime_anomaly_detection():
    st.title("Real-Time System Resource Usage Visualization and Anomaly Detection")

    # Select resource to visualize
    selected_resource = st.selectbox("Select Resource to Visualize", ["CPU Usage", "Memory Usage", "Disk Usage"])

    # Create a pandas DataFrame to store resource usage data
    resource_data = pd.DataFrame(columns=['Time', selected_resource])

    # Create a figure for plotly
    fig = go.Figure()

    # Initialize the chart with a scatter plot
    fig.add_trace(go.Scatter(x=resource_data['Time'], y=resource_data[selected_resource], mode='lines+markers',name=selected_resource, line=dict(color='royalblue')))

    # Set layout properties for a more visually appealing appearance
    fig.update_layout(title=f"Real-Time {selected_resource} Usage",
                      xaxis_title="Time",
                      yaxis_title=f"{selected_resource} Usage (%)",
                      template="plotly_dark",  # Dark theme
                      showlegend=True,
                      margin=dict(l=0, r=0, t=30, b=0),  # Adjust margins
                      autosize=True)

    chart = st.plotly_chart(fig)

    values_fetched = 0

    while values_fetched < 10:  # Collect the first 10 values
        # Get current time and system resource usage
        timestamp = time.time()
        indian_timezone = pytz.timezone('Asia/Kolkata')
        local_time = datetime.datetime.fromtimestamp(timestamp, indian_timezone)

        current_time = local_time.strftime("%H:%M:%S")
        cpu_usage, memory_usage, disk_usage = get_system_resources()

        # Update the chart data based on user selection
        resource_data = resource_data.append({'Time': current_time, selected_resource: cpu_usage},ignore_index=True)

        # Update the scatter plot
        fig.update_traces(x=resource_data['Time'], y=resource_data[selected_resource])

        # Update layout properties for a more visually appealing appearance
        fig.update_layout(title=f"Real-Time {selected_resource} Usage",
                          xaxis_title="Time",
                          yaxis_title=f"{selected_resource} Usage (%)",
                          template="plotly_dark",  # Dark theme
                          showlegend=True,
                          margin=dict(l=0, r=0, t=30, b=0),  # Adjust margins
                          autosize=True)

        # Display the chart
        chart.plotly_chart(fig)

        # Display the dataset only when all 10 values are fetched
        if values_fetched == 9:
            st.subheader(f"System Resource Usage Dataset (First 10 values) for {selected_resource}:")
            st.dataframe(resource_data)

            # Using PyCaret for anomaly detection
            exp_ano = setup(resource_data)
            iforest = create_model('iforest')

            # Predict with the model
            iforest_predictions = predict_model(iforest, data=resource_data)

            # Extract data for plotting 3D scatter plot
            x = resource_data['Time']
            y = resource_data[selected_resource]
            anomaly_scores = iforest_predictions['Anomaly_Score']

            # Create 3D scatter plot
            fig_3d = go.Figure(data=go.Scatter3d(
                x=x,
                y=y,
                z=anomaly_scores,  # Using anomaly scores as the third axis
                mode='markers',
                marker=dict(
                    size=10,  # Increase marker size
                    color=anomaly_scores,  # Color by anomaly score
                    opacity=0.8
                )
            ))

            # Update layout for 3D scatter plot
            fig_3d.update_layout(
                title=f'Anomalies Detected by Isolation Forest Model for {selected_resource}',
                scene=dict(
                    xaxis_title='Time',
                    yaxis_title=selected_resource,
                    zaxis_title='Anomaly Score'
                )
            )

            # Display 3D scatter plot
            st.plotly_chart(fig_3d)

            # Using PyCaret for anomaly detection
            exp_ano = setup(resource_data)
            iforest = create_model('iforest')

            # Predict with the model
            iforest_predictions = predict_model(iforest, data=resource_data)

            # Assign anomalies
            iforest_results = assign_model(iforest)

            # Display anomaly results
            st.subheader("Anomaly Detection Results")
            st.dataframe(iforest_results)

            # Evaluate the model (you can use different metrics based on your requirements)
            from sklearn.metrics import classification_report

            # Assuming 'Anomaly' is the target variable
            y_true = iforest_results['Anomaly']
            # Define a threshold for anomaly detection
            threshold = 0.5  # Adjust as needed based on your requirements

            # Convert continuous anomaly scores to binary labels
            y_pred_binary = (iforest_results['Anomaly_Score'] > threshold).astype(int)

            # Print classification report
            st.subheader("Model Evaluation Results")
            st.text(classification_report(y_true, y_pred_binary))


        # Increment the counter
        values_fetched += 1

        # Sleep for a short interval (e.g., 1 second)
        time.sleep(1)

def extract_features(log_text):
    cpu_pattern = r'CPU: (\d+)%'
    memory_pattern = r'Memory: (\d+)%'
    disk_pattern = r'Disk: (\d+)%'

    cpu_match = re.search(cpu_pattern, log_text)
    memory_match = re.search(memory_pattern, log_text)
    disk_match = re.search(disk_pattern, log_text)

    cpu_usage = int(cpu_match.group(1)) if cpu_match else None
    memory_usage = int(memory_match.group(1)) if memory_match else None
    disk_space = int(disk_match.group(1)) if disk_match else None

    return cpu_usage, memory_usage, disk_space

def apply_isolation_forest(df, column_name, contamination):
    iso_forest = IsolationForest(contamination=contamination, random_state=42)
    anomalies_iso_forest = iso_forest.fit_predict(df[[column_name]])
    df['Anomaly_Isolation_Forest'] = anomalies_iso_forest
    return df

def apply_local_outlier_factor(df, column_name, contamination):
    lof = LocalOutlierFactor(n_neighbors=20, contamination=contamination)
    anomalies_lof = lof.fit_predict(df[[column_name]])
    df['Anomaly_Local_Outlier_Factor'] = anomalies_lof
    return df

def main_logfile_anomaly_detection(uploaded_file):
    st.title("Log File Feature Extraction and Anomaly Detection")

    # uploaded_file = st.file_uploader("Upload log file", type=["log"])

    if uploaded_file is not None:
        log_content = uploaded_file.read().decode("utf-8")
        data = []
        for line in log_content.split("\n"):
            if "INFO" in line or "WARNING" in line:
                timestamp_match = re.search(r"\[(.*?)\]", line)
                if timestamp_match:
                    timestamp = timestamp_match.group(1)
                    cpu, memory, disk = extract_features(line)
                    data.append(
                        {
                            "Timestamp": timestamp,
                            "CPU Usage (%)": cpu,
                            "Memory Usage (%)": memory,
                            "Disk Space (%)": disk,
                        }
                    )

        df = pd.DataFrame(data)

        # Replace missing values with the mean
        df.fillna(df.mean(), inplace=True)

        st.write("### Extracted Dataset")
        st.write(df)

        if not df.empty:
            df["Timestamp"] = pd.to_datetime(
                df["Timestamp"], format="%Y-%m-%d %H:%M:%S"
            )
            df.set_index("Timestamp", inplace=True)
            contamination_slider = st.slider(
                "Select Contamination Value", 0.01, 0.10, 0.05, 0.01
            )

            fig_resource = px.line(
                df,
                x=df.index,
                y=["CPU Usage (%)", "Memory Usage (%)", "Disk Space (%)"],
                title="Resource Usage Over Time",
                labels={"value": "Percentage", "variable": "Resource"},
            )
            st.plotly_chart(fig_resource)

            # Values to try for contamination
            contamination_values = [0.1, 0.001, 0.002, 0.0003]

            best_contamination = None
            best_recall = 0

            for contamination in contamination_values:
                # Apply anomaly detection methods for CPU
                df_cpu = apply_isolation_forest(df.copy(), "CPU Usage (%)", contamination)
                df_cpu = apply_local_outlier_factor(
                    df_cpu, "CPU Usage (%)", contamination
                )

                # Calculate recall for Isolation Forest
                recall_iso_forest = np.sum(
                    (df_cpu["Anomaly_Isolation_Forest"] == -1)
                    & (df_cpu["CPU Usage (%)"] > df_cpu["CPU Usage (%)"].quantile(0.99))
                ) / np.sum(df_cpu["CPU Usage (%)"] > df_cpu["CPU Usage (%)"].quantile(0.99))

                # Update best contamination if recall is improved
                if recall_iso_forest > best_recall:
                    best_recall = recall_iso_forest
                    best_contamination = contamination

            st.write(f"Best Contamination Value for CPU: {best_contamination}")

            # Apply the best contamination value for CPU
            df_cpu = apply_isolation_forest(df.copy(), "CPU Usage (%)", contamination_slider)
            df_cpu = apply_local_outlier_factor(df_cpu, "CPU Usage (%)", best_contamination)

            df_memory = apply_isolation_forest(df.copy(), "Memory Usage (%)", best_contamination)
            df_memory = apply_local_outlier_factor(df_memory, "Memory Usage (%)", best_contamination)

            df_disk = apply_isolation_forest(df.copy(), "Disk Space (%)", best_contamination)
            df_disk = apply_local_outlier_factor(df_disk, "Disk Space (%)", best_contamination)

            fig_cpu = px.line(
                df_cpu,
                x=df_cpu.index,
                y=["CPU Usage (%)"],
                title="Anomaly Detection - CPU Usage Over Time",
                labels={"value": "Percentage", "variable": "Resource"},
            )

            fig_cpu.add_scatter(
                x=df_cpu[df_cpu["Anomaly_Isolation_Forest"] == -1].index,
                y=df_cpu[df_cpu["Anomaly_Isolation_Forest"] == -1]["CPU Usage (%)"],
                mode="markers",
                marker=dict(color="red"),
                name="Isolation Forest Anomalies",
            )

            fig_cpu.add_scatter(
                x=df_cpu[df_cpu["Anomaly_Local_Outlier_Factor"] == -1].index,
                y=df_cpu[df_cpu["Anomaly_Local_Outlier_Factor"] == -1]["CPU Usage (%)"],
                mode="markers",
                marker=dict(color="blue"),
                name="Local Outlier Factor Anomalies",
            )

            st.plotly_chart(fig_cpu)

            fig_memory = px.line(
                df_memory,
                x=df_memory.index,
                y=["Memory Usage (%)"],
                title="Anomaly Detection - Memory Usage Over Time",
                labels={"value": "Percentage", "variable": "Resource"},
            )
            fig_memory.add_scatter(x=df_memory[df_memory['Anomaly_Isolation_Forest'] == -1].index,
                                   y=df_memory[df_memory['Anomaly_Isolation_Forest'] == -1]['Memory Usage (%)'],
                                   mode='markers',
                                   marker=dict(color='red'),
                                   name='Isolation Forest Anomalies')

            fig_memory.add_scatter(x=df_memory[df_memory['Anomaly_Local_Outlier_Factor'] == -1].index,
                                   y=df_memory[df_memory['Anomaly_Local_Outlier_Factor'] == -1]['Memory Usage (%)'],
                                   mode='markers',
                                   marker=dict(color='blue'),
                                   name='Local Outlier Factor Anomalies')

            st.plotly_chart(fig_memory)

            # Plot resource usage over time with anomalies for Disk
            fig_disk = px.line(df_disk, x=df_disk.index, y=['Disk Space (%)'],
                               title='Anomaly Detection - Disk Space Over Time',
                               labels={'value': 'Percentage', 'variable': 'Resource'})

            fig_disk.add_scatter(x=df_disk[df_disk['Anomaly_Isolation_Forest'] == -1].index,
                                 y=df_disk[df_disk['Anomaly_Isolation_Forest'] == -1]['Disk Space (%)'],
                                 mode='markers',
                                 marker=dict(color='red'),
                                 name='Isolation Forest Anomalies')

            fig_disk.add_scatter(x=df_disk[df_disk['Anomaly_Local_Outlier_Factor'] == -1].index,
                                 y=df_disk[df_disk['Anomaly_Local_Outlier_Factor'] == -1]['Disk Space (%)'],
                                 mode='markers',
                                 marker=dict(color='blue'),
                                 name='Local Outlier Factor Anomalies')

            st.plotly_chart(fig_disk)

            # Display the dataframes with anomalies
            st.write('### Dataset with Anomalies Detected - CPU')
            st.write(df_cpu)

if __name__ == "__main__":
    main()
