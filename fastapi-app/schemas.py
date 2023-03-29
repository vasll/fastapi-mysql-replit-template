from sqlalchemy import Column, Integer, String, Text
from database import Base

class Item(Base):
	""" Represents the items schema in the database. For demonstration purposes """
	__tablename__ = "items"
	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	name = Column(String(128), nullable=False)
	description = Column(Text, nullable=True)