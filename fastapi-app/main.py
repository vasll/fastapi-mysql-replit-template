from fastapi import FastAPI
from database import get_database, engine
from fastapi import Depends
from sqlalchemy.orm import Session
import uvicorn
import schemas


#FastAPI
app = FastAPI()
schemas.Base.metadata.create_all(bind=engine)  # Create all db tables if they don't exist on startup

# Routes
@app.get("/")
async def index(db:Session = Depends(get_database)):
	db_users = [user for user in db.query(schemas.User).all()]  # Fetch all users from db
	return {
		'detail': 'FastAPI is working',
		'users': db_users
	}


# Run the uvicorn development web server. 
# Code from: https://www.uvicorn.org/deployment/
if __name__ == "__main__":
	uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True)
	