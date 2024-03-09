
import mysql.connector
from dotenv import load_dotenv
import os
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import RequestResponseEndpoint
import pyodbc

import dbsecure.mysql
# Load environment variables
load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

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
    connection=dbsecure.mysql.Connection()
    return await connection.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    # return dbsecure.pyodbc.connect(
    #      "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=uconnect;UID=shrikant;PWD=Rudolf@123;TrustServerCertificate=yes"
    # )
async def create(id:int):
    try:
        conn =await connect()
        print(conn)
        print(type(conn))
        print("hereeeeee")
        cursor = conn.cursor()
        print('cursor created')
        # check if cursor is of type pyodbc
        query = 'INSERT INTO test VALUES (%s)'
        values = (id,)
        print(cursor)
        print(type(cursor))
        await cursor.execute(query,values)
        conn.commit()
        await conn.close()
        return 1
    except Exception as e:
        print(e)

class DatabaseQueryInterceptorMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        try:
            raw_query = get_raw_query_from_request(request)
            processed_query = process_query_with_interceptor(raw_query)
            set_raw_query_to_request(request, processed_query)
            response = await call_next(request)
            return response
        except Exception as e:
            raise e

def get_raw_query_from_request(request: Request) -> str:
    # Implement logic to extract raw query from the request
    # For example, if using SQLAlchemy, you might access the query from request state
    return getattr(request.state, "db_query", "")


def set_raw_query_to_request(request: Request, query: str):
    # Implement logic to set the processed query back to the request
    # For example, if using SQLAlchemy, you might set it in request state
    request.state.db_query = query 


def process_query_with_interceptor(raw_query: str) -> str:
    # Implement logic to intercept and modify the query
    # For example, you can add a comment to the query
    return f"/* Interceptor added */ {raw_query}"


