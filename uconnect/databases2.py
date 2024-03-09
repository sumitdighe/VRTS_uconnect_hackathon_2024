# from sqlalchemy import URL, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://shrikant:password@localhost:3306/uconnect"
# SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://shrikant:Rudolf@123@127.0.0.1:1433/uconnect?driver=ODBC+Driver+18+for+SQL+Server"
# connection_url = URL.create(
#     "mssql+pyodbc",
#     username="shrikant",
#     password="Rudolf@123",
#     host="localhost",
#     port=1433,
#     database="uconnect",
#     query={
#         "driver": "ODBC Driver 18 for SQL Server",
#         "TrustServerCertificate": "yes",
#         # "authentication": "ActiveDirectoryIntegrated",
#     },
# )
# engine = create_engine(
#     connection_url
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

