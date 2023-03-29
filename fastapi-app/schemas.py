from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
	""" Represents the user schema """
	__tablename__ = "users"
	id = Column(Integer, primary_key=True, index=True, autoincrement=True)
	nickname = Column(String(16), nullable=False, unique=True)
	email = Column(String(320), nullable=False, unique=True)
	password = Column(String(255), nullable=False, unique=True)