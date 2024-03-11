import json
import dbsecure as dbs
import asyncio
import websockets
import pyodbc
class Connection(dbs.Connection):
    async def connect(self,conn,**kwargs):
        json_data=json.dumps({
            'action':'connect',
            'ip':dbs.Connection.get_server_ip(),
            'user':kwargs['user'],
            'params':kwargs,
        })
        self.user=kwargs['user']
        self.ws=await websockets.connect(self.url)
        await self.ws.send(json_data)
        response=await self.ws.recv()
        print(response)
        print('connection sent')
        conn=pyodbc.connect(conn)
        self.connection=conn
        return self