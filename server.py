from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

latest_location = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/location")
async def receive_location(data: dict):
    global latest_location
    latest_location = data

    print("GPS:", data)

    return {"status": "ok"}

@app.get("/location")
async def get_location():
    return latest_location
