# DBSecure
### A lightweight server-database proxy which sees it all

## Features:
### 1. Database independent: 
  Not dependent on any database specific syntax or query format.
### 2. Unsupervised Anomaly Detection:
  Uses a continous learning autoencoder-decoder with just 3 layers to identify anomalous queries
### 3. Bidirectional Security:
  Has filters on both incoming queries and outgoing results
### 4. Frequency Monitoring
  Notifies sudden surges in database requests
### 5. Location Monitoring
  Monitors and logs IP addresses of requests
### 6. Statistics Anomaly Detection
  Calculates the delay in response, the result size and the amount of modified data and detects unusual metrics
### 7. Fully Customizable
  Users can add their own rules and thresholds
  
## Sample anomaly log:
```WARNING:root:New IP logged: 172.21.216.29
WARNING:root:New query class (INSERT INTO test VALUES (%s)) detected for user shrikant
WARNING:root:High request frequency detected: 29.00 requests/second
WARNING:root:New query class (SELECT * FROM test) detected for user shrikant
WARNING:root:New query class (SELECT SLEEP(3)) detected for user shrikant
WARNING:root:High request frequency detected: 3.00 requests/second
WARNING:root:Anomaly detected: Delay (18.52) exceeds threshold (2.00)
WARNING:root:High request frequency detected: 4.00 requests/second
WARNING:root:New query class (with recursive rnums as (
        select 1 as n
            union all
        select n+1 as n from rnums
         where n <101
        )
    select * from rnums
    ;) detected for user shrikant
WARNING:root:Anomaly detected: Delay (52.72) exceeds threshold (2.00)
WARNING:root:Output result size anomalous; 101 rows fetched
WARNING:root:New query class (INSERT INTO test VALUES (?)) detected for user shrikant
```
