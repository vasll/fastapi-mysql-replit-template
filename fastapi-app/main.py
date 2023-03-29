from fastapi import FastAPI
from database import get_database, engine
from fastapi import Depends
from sqlalchemy.orm import Session
import uvicorn
import schemas

#FastAPI
app = FastAPI()
schemas.Base.metadata.create_all(bind=engine)  # [OPTIONAL] Create all db tables present in schemas.py if they don't exist


# Routes
@app.get("/")
async def index(db:Session = Depends(get_database)):
	database_items = db.query(schemas.Item).all()  # Fetch all items from db
	return {
		'detail': 'FastAPI is working',
		'items': database_items
	}


# Run the uvicorn development web server
# Code from: https://www.uvicorn.org/deployment/
if __name__ == "__main__":
	uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True)
	