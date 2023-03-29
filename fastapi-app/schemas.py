from sqlalchemy import Column, Integer, String, Text
from database import Base

# This file contains the database schemas (tables) in the database. By default if a new schema is created in this script, it will be added
# to the database thanks to the expression 'schemas.Base.metadata.create_all(bind=engine)' in main.py

class Item(Base):
	""" Represents the 'items' schema in the database. (For demonstration purposes) """
	__tablename__ = "items"
	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String(128), nullable=False)
	description = Column(Text, nullable=True)