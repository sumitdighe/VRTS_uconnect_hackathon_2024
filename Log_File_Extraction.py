import streamlit as st
import pandas as pd
import re
import matplotlib.pyplot as plt

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

def main():
    st.title('Log File Feature Extraction')

    uploaded_file = st.file_uploader("Upload log file", type=['log'])

    if uploaded_file is not None:
        log_content = uploaded_file.read().decode('utf-8')
        data = []
        for line in log_content.split('\n'):
            if 'INFO' in line or 'WARNING' in line:
                timestamp_match = re.search(r'\[(.*?)\]', line)  # Search for timestamp within square brackets
                if timestamp_match:
                    timestamp = timestamp_match.group(1)
                    cpu, memory, disk = extract_features(line)
                    data.append({'Timestamp': timestamp, 'CPU Usage (%)': cpu, 'Memory Usage (%)': memory, 'Disk Space (%)': disk})

        df = pd.DataFrame(data)
        st.write('### Extracted Dataset')
        st.write(df)

        if not df.empty:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d %H:%M:%S') 
            df.set_index('Timestamp', inplace=True)  
            plt.figure(figsize=(10, 6))
            df.plot(ax=plt.gca()) 
            plt.xlabel('Time')
            plt.ylabel('Percentage')
            plt.title('Resource Usage Over Time')
            st.pyplot(plt)

if __name__ == '__main__':
    main()
