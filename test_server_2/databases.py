
import mysql.connector
from dotenv import load_dotenv
import os
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import RequestResponseEndpoint
import pyodbc
import dbsecure.pyodbc



load_dotenv()

# Connect to MySQL
async def connect():
    # return pyodbc.connect(
    #     "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=uconnect;UID=shrikant;PWD=Rudolf@123;TrustServerCertificate=yes"
    # )
    # return mysql.connector.connect(
    #     host=MYSQL_HOST,
    #     user=MYSQL_USER,
    #     password=MYSQL_PASSWORD,
    #     database=MYSQL_DB
    # )
    connection=dbsecure.pyodbc.Connection()
    return await connection.connect(
         "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=uconnect;UID=shrikant;PWD=Rudolf@123;TrustServerCertificate=yes"
         ,user='shrikant',
    )
async def create(id:int):
    try:
        conn =await connect()
        print(conn)
        print(type(conn))
        print("hereeeeee")
        cursor = conn.cursor()
        print('cursor created')
        query = 'INSERT INTO test VALUES (?)'
        values = id
        print(cursor)
        print(type(cursor))
        await cursor.execute(query,(values,))
        conn.commit()
        await conn.close()
        return 1
    except Exception as e:
        print(e.with_traceback())

async def frequency_hit():
    query='INSERT INTO test VALUES (%s)'
    conn=await connect()
    cursor=conn.cursor()
    for i in range(10):
        values=(i,)
        await cursor.execute(query,values)
    conn.commit()
    await conn.close()

async def delay_hit():
    query='SELECT * FROM test'
    conn=await connect()
    cursor=conn.cursor()
    print('sending request 1')
    result=await cursor.execute(query,())
    print('sending request 2')
    query='SELECT SLEEP(3)'
    await cursor.execute(query,()) 
    await conn.close()
    return result
        
async def volume_hit():
    query="""with recursive rnums as (
        select 1 as n
            union all
        select n+1 as n from rnums
         where n <101
        )
    select * from rnums
    ;"""
    conn=await connect()
    cursor=conn.cursor()
    result=await cursor.execute(query,())
    await conn.close()
    return result
