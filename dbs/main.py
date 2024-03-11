import time
from fastapi import Depends, FastAPI, HTTPException, WebSocket
import json
import numpy as np
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
import logging
from collections import deque
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow.compat.v1 as tf
from tensorflow.keras import metrics
from model import create_decoder

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('ERROR')
logging.basicConfig(filename='app.log', level=logging.INFO)
load_dotenv()
engine = create_engine('sqlite:///db.sqlite')  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Connection(Base):
  __tablename__ = "connections"
  id = Column(Integer, primary_key=True)
  ip = Column(String, unique=True)

class ConnectionData(Base):
  __tablename__ = "connection_data"
  id = Column(Integer, primary_key=True)
  user = Column(String)
  query = Column(Text)
  count=Column(Integer)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


def is_new_ip(db, ip):
  result = db.query(Connection).filter_by(ip=ip).first()
  if not result:
    new_connection = Connection(ip=ip)
    db.add(new_connection)
    db.commit()
    logging.warn(f"New IP logged: {ip}")

def store_connection_data(db, user, query):
  existing_record = db.query(ConnectionData) \
                     .filter(ConnectionData.user == user, ConnectionData.query == query) \
                     .first()

  if existing_record:
    existing_record.count = existing_record.count + 1
  else:
    new_connection_data = ConnectionData(user=user, query=query, count=1)
    logging.warn(f'New query class ({query}) detected for user {user}')
    db.add(new_connection_data)
  db.commit()





@app.websocket("/dbsecure")
async def get_connection(websocket: WebSocket, db: Session = Depends(get_db)):
  delays=deque(maxlen=10)
  mean_delay=0
  requests=0
  start_time=1000
  request_threshold = os.getenv('REQUEST_THRESHOLD')
  await websocket.accept()
  try:
    while True:
      data = await websocket.receive_text()
      dict_data = json.loads(data)
      if dict_data["action"] == "connect":
            start_time = time.time()
            requests=0
            user = dict_data["user"]
            ip = dict_data["ip"]
            is_new_ip(db, ip)  
            await websocket.send_text(json.dumps({"flag": True}))
      elif dict_data["action"] == "query":
            requests+=1
            if requests>=1:
              elapsed_time = time.time() - start_time
              print(elapsed_time)
              request_rate = int(requests /elapsed_time)
              if requests==10:
                requests=0
                start_time=time.time()
              if request_rate > int(request_threshold):
                logging.warning(f"High request frequency detected: {request_rate:.2f} requests/second")
              user = dict_data["user"]
            query = dict_data["query"]
            store_connection_data(db, user, query) 
            get_recon_error(query)
            if not preliminary_check(query,user):await websocket.send_text(json.dumps({"flag": False}))
            await websocket.send_text(json.dumps({"flag":True}))
      elif dict_data['action']=='result':
            new_delta=dict_data['delta']*100
            res_size=len(dict_data['fetch'])
            count=dict_data['count']
            print(dict_data)
            output_check(new_delta,res_size,count,delays,mean_delay)

      else:
        raise HTTPException(status_code=400, detail="Invalid action")
  except Exception as e:
    print(e.with_traceback())
def preliminary_check(query,user):
  keywords=query.split()
  if 'DROP' in keywords or 'DELETE' in keywords:
    logging.warn(f"Potentially privileged instruction ({query}) run by {user}")
  return 1

def output_check(delay,res_size,count,delays,mean_delay):
   update_and_check(delay,delays,mean_delay)
   if res_size>int(os.getenv('SIZE_THRESHOLD')):
    logging.warn(f"Output result size anomalous; {res_size} rows fetched")
    if count>os.getenv('COUNT_THRESHOLD'):
      logging.warn(f"Affected row count anomalous; {count} rows affected")

def update_and_check(new_delay,delays,mean_delay):
  delays.append(new_delay)
  mean_delay = int(sum(delays) / len(delays) ) 
  if len(delays) == 1: mean_delay=1
  if new_delay > mean_delay *int(os.getenv('DELAY_THRESHOLD')):
    logging.warn(f"Anomaly detected: Delay ({new_delay:.2f}) exceeds threshold ({mean_delay *int(os.getenv('DELAY_THRESHOLD')):.2f})")
    return True
  else:
    return False

def get_recon_error(query):
  model=create_decoder((100,100))
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=[metrics.Accuracy(), 'mse'])
  model.load_weights('model.h5')
  tokenizer=Tokenizer()
  sequences = tokenizer.texts_to_sequences([query]) 
  padded_sequence = pad_sequences(sequences, maxlen=100, padding='post')  
  one_hot_encoded_input = tf.one_hot(padded_sequence, 100) 
  reconstructed_input = model.predict(one_hot_encoded_input)
  reconstruction_error = tf.keras.losses.categorical_crossentropy(one_hot_encoded_input, reconstructed_input)
  reconstruction_error = np.mean(reconstruction_error.numpy())  
  print("Reconstruction error:", reconstruction_error)
  if reconstruction_error >int(os.getenv('RECONSTRUCTION_THRESHOLD')):
    logging.warn(f"Anomaly detected: Reconstruction error ({reconstruction_error:.2f}) exceeds threshold (0.01)")

def send_email(message):
  # sender_email =os.getenv('SENDER_MAIL')
  # sender_password =''
  # receiver_email = "recipient@example.com"
  # msg = MIMEText(message, 'plain')
  # msg['Subject'] = "Anomaly Alert"+str(time.time())
  # msg['From'] = sender_email
  # msg['To'] = receiver_email
  # smtp_server = "smtp.example.com" 
  # port = 587 
  # server = smtplib.SMTP(smtp_server, port)
  # server.starttls()

  # # Login with credentials
  # server.login(sender_email, sender_password)

  # # Send the email
  # server.sendmail(sender_email, receiver_email, msg.as_string())
  # server.quit()

  # print("Email sent successfully!")
  pass