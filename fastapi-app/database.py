import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database credentials
# Username, password and database_name are loaded from secrets/envvars
username = os.getenv('db_user')
password = os.getenv('db_pass')
database_name = os.getenv('db_name')
address = '127.0.0.1'
port = '3306'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{address}:{port}/{database_name}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Database dependency [https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-dependency]
def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()