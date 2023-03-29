import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database credentials, picked from replit secrets
username = os.getenv('db_user')
password = os.getenv('db_pass')
address = '127.0.0.1'
port = '3306'
database_name = os.getenv('db_name')

engine = create_engine(f'mysql+pymysql://{username}:{password}@{address}:{port}/{database_name}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()