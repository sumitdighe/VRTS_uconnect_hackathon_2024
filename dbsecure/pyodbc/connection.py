import dbsecure as dbs
import asyncio
import websockets
import mysql.connector
import pyodbc
class Connection(dbs.Connection):
    async def connect(self,**kwargs):
        self.ws=await websockets.connect(self.url)
        await self.ws.send(str(kwargs))
        response=await self.ws.recv()
        print(response)
        conn=mysql.connector.connect(**kwargs)
        self.connection=conn
        return self