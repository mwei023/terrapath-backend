from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime


app = FastAPI()


latest_location = {}

events = []

alerts = []


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/location")
async def receive_location(data: dict):

    global latest_location

    data["timestamp"] = str(datetime.now())

    latest_location = data

    events.append(data)

    print("GPS:", data)

    return {
        "status": "received"
    }



@app.get("/location")
async def get_location():

    return latest_location




@app.get("/events")
async def get_events():

    return events



@app.post("/alert")
async def create_alert(data: dict):

    data["timestamp"] = str(datetime.now())

    alerts.append(data)

    print("ALERT:", data)

    return {
        "status": "alert stored"
    }



@app.get("/alerts")
async def get_alerts():

    return alerts
