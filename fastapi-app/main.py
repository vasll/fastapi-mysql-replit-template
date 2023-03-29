from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError
from database import get_database, engine
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
import uvicorn
import schemas
import models

#FastAPI
app = FastAPI()
schemas.Base.metadata.create_all(bind=engine)  # [OPTIONAL] Create all db tables present in schemas.py if they don't exist


# Routes
@app.get("/")
async def get_items(db:Session = Depends(get_database)):
	""" """
	database_items = db.query(schemas.Item).all()  # Fetch all items from db
	return {
		'detail': 'FastAPI is working',
		'items': database_items
	}


@app.post("/", response_model=List[models.Item])
async def insert_item(item: models.Item, db:Session = Depends(get_database)):
	""" """
	db.add(schemas.Item(id=item.id, name=item.name, description=item.description))
	
	try:
		db.commit()
	except IntegrityError as _:
		return {'detail': 'Integrity error. Item with that id already exists'}
	
	return [i.__dict__ for i in db.query(schemas.Item).all()]	# Return all items
		

# Run the uvicorn development web server
# Code from: https://www.uvicorn.org/deployment/
if __name__ == "__main__":
	uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True)
	