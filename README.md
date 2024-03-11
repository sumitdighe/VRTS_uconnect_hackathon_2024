## **VRTS_uconnect_hackathon_2024**

## **AI Powered Anomaly Detection System**

### **Overview**
This repository contains code for an Anomaly Detection System built using Streamlit. The system can analyze CSV data, log files, or real-time system resource usage to detect anomalies. It leverages machine learning models such as Isolation Forest, Local Outlier Factor, Z-score along with Pycaret library for anomaly detection.

### **Installation Steps**

To run the Anomaly Detection System, follow these steps:
1.	Install the required Python packages:
!pip install streamlit, pycaret, streamlit_lottie, pytz 

2. Create a file named app.py and all your code in this file.

3.	Execute the command in a terminal or shell environment, it will retrieve and display the public IPv4 address of the machine. Copy the address generated in the tunnel website

!wget -q -O - ipv4.icanhazip.com

4.	Run the Streamlit app and localtunnel for exposing the web application:
! streamlit run app.py & npx localtunnel --port 8501

### **Usage**

1.	Access the Streamlit app by opening the provided localtunnel link.
2.	Select the data type (Log File Data, Realtime Data, or CSV Data) from the sidebar.
3.	If you choose "CSV Data," upload a CSV file containing the data you want to analyze. Select the X-axis and Y-axis columns, choose an anomaly detection method (Z-Score, Isolation Forest, or Local Outlier Factor), and set the contamination value if applicable.
4.	If you choose "Log File Data," upload a log file to extract features and perform anomaly detection.
5.	If you choose "Realtime Data," the system displays real-time system resource usage visualization and anomaly detection. You can select the resource (CPU Usage, Memory Usage, Disk Usage) to visualize.


### **Features**

1. Anomaly detection for CSV data, log files, and real-time system resource usage.
2. Multiple anomaly detection methods available
3. Real-time visualization of system resource usage with anomaly detection results.

### Feel free to contribute, report issues, or suggest improvements. Happy Coding :smile:



