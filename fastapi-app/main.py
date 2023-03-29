from fastapi import FastAPI
import database
import uvicorn


app = FastAPI()


@app.get("/")
async def index():
    return {'detail': 'FastAPI is working'}


# Run the uvicorn web server
if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")