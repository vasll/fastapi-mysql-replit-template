from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError
from database import get_database, engine
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import uvicorn
import schemas
import models

# This file is the entry point of the api
# For demonstration purposes some routes, models and schemas were added, feel free to delete them and make your own

# FastAPI setup
app = FastAPI()
schemas.Base.metadata.create_all(bind=engine)  # [OPTIONAL] Create all db tables present in schemas.py if they don't exist

# Routes
@app.get("/", description="API index")
async def index():
	return {
		'description': "To get started visit the FastAPI docs at [https://fastapi.tiangolo.com] or explore this template API"
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
if __name__ == "__main__":
	# Introduction text
	print("\n\nHello from FastAPI! To get started visit the FastAPI docs at [https://fastapi.tiangolo.com] or explore this example API's docs by going to [https://your_repl_url/docs] (you can find the repl's url from the webview tab in tools)\n\n")

	# Start the server, to access it use your repl's url, you can find it in the webview tab. Code from: [https://www.uvicorn.org/deployment/]
	uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True)	

	