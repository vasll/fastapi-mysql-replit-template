from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {'working': True}