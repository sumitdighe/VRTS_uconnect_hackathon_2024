import time
from fastapi import Depends, FastAPI, HTTPException, WebSocket
import json
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
import logging
from collections import deque
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
logging.basicConfig(filename='app.log', level=logging.INFO)
load_dotenv()
engine = create_engine('sqlite:///db.sqlite')  # Replace with your connection string
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
request_queue = deque(maxlen=10)  
request_threshold = 5 
@app.websocket("/dbsecure")
async def get_connection(websocket: WebSocket, db: Session = Depends(get_db)):
  await websocket.accept()
  try:
    start_time = time.time()  
    while True:
      data = await websocket.receive_text()
      request_queue.append(time.time())  
      dict_data = json.loads(data)
      if dict_data["action"] == "connect":
            user = dict_data["user"]
            ip = dict_data["ip"]
            is_new_ip(db, ip)  
            await websocket.send_text(json.dumps({"flag": True}))
      elif dict_data["action"] == "query":
            user = dict_data["user"]
            query = dict_data["query"]
            store_connection_data(db, user, query) 
            if not anomaly_check():await websocket.send_text(json.dumps({"flag": False}))
            await websocket.send_text(json.dumps({"flag":True}))
      else:
        raise HTTPException(status_code=400, detail="Invalid action")
  except Exception as e:
    print(e)

def anomaly_check():return True


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