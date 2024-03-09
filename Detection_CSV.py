import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import LocalOutlierFactor
import numpy as np

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

    test_data['score_lof'] = -scores_lof  # Make scores positive for consistency

    lof_threshold = test_data['score_lof'].quantile(0.95)  # Example: 95th percentile
    test_data['anomaly_lof'] = np.where(test_data['score_lof'] > lof_threshold, -1, 1)

    df_result = pd.concat([train_data, test_data])

    return df_result

def identify_anomalies(df, x_col, y_col, detection_method, contamination_iso):
    if detection_method == 'Z-Score':
        df = calculate_zscore_mad(df, y_col)
        anomalies_df = df[(df['z_score'] > 2) | (df['z_score'] < -2)]
        st.subheader('Anomalies Detected by Z-Score:')
        st.write(f'Total Anomalies (Z-Score): {len(anomalies_df)}')
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
        anomaly_threshold = df[y_col].quantile(0.99)  # Example: 99th percentile
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
        cm = confusion_matrix(df['label'], np.where(df['z_score'] > 2, 1, 0))
        st.subheader('Confusion Matrix for Z-Score:')
    elif detection_method == 'Isolation Forest':
        cm = confusion_matrix(df['label'], np.where(df['anomaly_iforest'] == -1, 1, 0))
        st.subheader('Confusion Matrix for Isolation Forest:')
    elif detection_method == 'Local Outlier Factor':
        cm = confusion_matrix(df['label'], np.where(df['anomaly_lof'] == -1, 1, 0))
        st.subheader('Confusion Matrix for Local Outlier Factor:')

    st.table(pd.DataFrame(cm, columns=['Predicted Normal', 'Predicted Anomaly'], index=['Actual Normal', 'Actual Anomaly']))

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
    st.title('CPU Utilization Analysis')

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

        if detection_method == 'Isolation Forest':
            initial_contamination_iso = 1 / len(df)
            contamination_iso_text = st.text_input('Enter Contamination Value (between 0 and 0.5):', initial_contamination_iso)
            contamination_iso = float(contamination_iso_text) if contamination_iso_text else 0  # Default to 0 if the field is empty

        else:
            contamination_iso = 0  # Not used for Z-Score or Local Outlier Factor

        df['label'] = 0  # Assume all data points are normal

        identify_anomalies(df, x_col, y_col, detection_method, contamination_iso)

if __name__ == "__main__":
    main()
