
# import mysql.connector

# def store_network_traffic(data):
#     # Replace these with your actual database connection parameters
#     conn_params = {
#         'database': 'NetworkInfo',
#         'user': 'root',
#         'password': 'Abhi@3112',
#         'host': 'localhost'
#     }
#     conn = mysql.connector.connect(**conn_params)
#     cursor = conn.cursor()

#     insert_query = """
#     INSERT INTO network_traffic_analysis (source_ip, destination_ip, transferred_data, timestamp, recommendation)
#     VALUES (%s, %s, %s, %s, %s)
#     """
#     for record in data:
#         recommendation = generate_auto_scaling_recommendation(record['transferred_data'])
        
#         cursor.execute(insert_query, (
#             record['source_ip'], 
#             record['destination_ip'],
#             record['transferred_data'], 
#             record['timestamp'],
#             recommendation
#         ))
    
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Make sure to update the rest of your script accordingly.

# def generate_auto_scaling_recommendation(transferred_data):
#     if transferred_data > 1000:  
#         return "Increase server capacity"
#     else:
#         return "Maintain current capacity"

# if __name__ == "__main__":
#     network_traffic_data = [
#         {'source_ip': '192.168.1.1', 'destination_ip': '10.0.0.1', 'transferred_data': 500, 'timestamp': '2024-03-10 12:00:00'},
#     ]
    
#     store_network_traffic(network_traffic_data)
import mysql.connector
from scapy.all import sniff

def store_network_traffic(pkt):
    # Replace these with your actual database connection parameters
    conn_params = {
        'database': 'NetworkInfo',
        'user': 'root',
        'password': 'Abhi@3112',
        'host': 'localhost'
    }
    conn = mysql.connector.connect(**conn_params)
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO network_traffic_analysis (source_ip, destination_ip, transferred_data, timestamp, recommendation)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    # Extract relevant information from the packet
    source_ip = pkt[0][1].src
    destination_ip = pkt[0][1].dst
    transferred_data = len(pkt)
    timestamp = pkt.time
    recommendation = generate_auto_scaling_recommendation(transferred_data)

    # Insert the data into the database
    cursor.execute(insert_query, (
        source_ip, 
        destination_ip,
        transferred_data, 
        timestamp,
        recommendation
    ))
    
    conn.commit()
    cursor.close()
    conn.close()

def generate_auto_scaling_recommendation(transferred_data):
    if transferred_data > 1000:  
        return "Increase server capacity"
    else:
        return "Maintain current capacity"

if __name__ == "__main__":
    # Start capturing network traffic in real-time
    sniff(prn=store_network_traffic)
