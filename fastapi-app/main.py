from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError
from database import get_database, engine
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uvicorn
import schemas
import models

#FastAPI
app = FastAPI()
schemas.Base.metadata.create_all(bind=engine)  # [OPTIONAL] Create all db tables present in schemas.py if they don't exist


# Routes
@app.get("/", description="page index")
async def index():
	return {
		'detail': 'FastAPI is working!',
		'description': "To get started visit the FastAPI docs or explore this example API's docs by going to https://[YOUR REPL URL]/docs",
		'fastapi_docs': 'https://fastapi.tiangolo.com/'
	}


@app.get("/items/", tags=['items'], response_model=List[models.Item], description="Gets all items from the 'items' table")
async def get_items(db:Session = Depends(get_database)):
	items = db.query(schemas.Item).all()  # Get all items from db
	return [i.__dict__ for i in items]	#  Return all items as dicts inside of a List


@app.post("/items/", tags=['items'], response_model=List[models.Item], description="Inserts an item into the 'items' table")
async def insert_item(item: models.Item, db:Session = Depends(get_database)):
	db.add(schemas.Item(id=item.id, name=item.name, description=item.description))
	
	try:
		db.commit()
	except IntegrityError as _:
		raise HTTPException(status_code=422, detail=f'Integrity error: Item with id {item.id} already exists')
	
	items = db.query(schemas.Item).all()  # Get all items from db
	return [i.__dict__ for i in items]	#  Return all items as dicts inside of a List
		

# Run the uvicorn development web server
# Code from: https://www.uvicorn.org/deployment/
if __name__ == "__main__":
	uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True)
	