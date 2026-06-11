from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime


app = FastAPI()


vehicles = {}

events = []

alerts = []

DEVICE_KEYS = {
    "TP-0001": "TP_DEV_KEY_001"
}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/location")
async def receive_location(
    data: dict,
    x_device_key: str = Header(None)
):

    vehicle_id = data.get("vehicle")
    if not vehicle_id:
        raise HTTPException(
            status_code=400,
            detail="Vehicle ID required"
            )
        
        expected_key = DEVICE_KEYS.get(vehicle_id)
        
    if expected_key is None:
        raise HTTPException(
            status_code=401,
            detail="Unknown device"
            )
            
    if x_device_key != expected_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid device key"
            )

    if not vehicle_id:
        return {
            "error": "vehicle ID required"
        }

    event = {
        "vehicle": vehicle_id,
        "lat": data.get("lat"),
        "lng": data.get("lng"),
        "speed": data.get("speed"),
        "bearing": data.get("bearing"),
        "timestamp": str(datetime.now())
    }

    # Current position of this vehicle
    vehicles[vehicle_id] = event

    # Historical record
    events.append(event)

    print(
        "GPS:",
        vehicle_id,
        event
    )

    return {
        "status": "received"
    }



@app.get("/location")
async def get_locations():

    return vehicles




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
