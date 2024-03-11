import json
import socket
import time
from dotenv import load_dotenv
import os
import asyncio
import websockets
load_dotenv()
class Cursor:
    def __init__(self,ws,connection,user):
        self.ws=ws
        self.connection=connection
        self.original_cursor=None
        self.user=user
    async def execute(self,query,value):
       self. original_cursor=self.connection.cursor()
       print(type(self.original_cursor))
       await self.ws.send(json.dumps({'action':'query','user':self.user,'query':query}))
       response=await self.ws.recv()
       data=json.loads(response)
       print(data)
       if(data['flag']):
            try:
                print(f'executing {query}')
                start_time=time.time()
                self.original_cursor.execute(query,value)
                delta=time.time()-start_time
                count=self.original_cursor.rowcount
                fetch=self.original_cursor.fetchall()
                print(delta,count,fetch)
                await self.ws.send(json.dumps({'action':'result','delta':delta,'fetch':fetch,'count':count}))
                await self.ws.recv()
            except Exception as e:
                print(e)
       return self.original_cursor
class Connection:
    def __init__(self) -> None:
        self.connection=None
        self.url=os.getenv('DBSEC_URL')
        self.mod_cursor=None
        self.ws=None
        self.event_loop=None
        self.user=""
    async def connect(self):
        pass
    def cursor(self):
        print('heeree')
        self.mod_cursor=Cursor(self.ws,self.connection,self.user)
        return self.mod_cursor
    def commit(self):
        self.connection.commit()
    async def close(self):
        await self.ws.close()
        self.connection.close()
    def get_server_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  
        return s.getsockname()[0] 

