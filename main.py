from fastapi import FastAPI, HTTPException
from schema import Request, Response, Vehicle
from assemble import find_vehicle

app = FastAPI()

@app.post("/find_vehicles", response_model=Response)
def find_vehicles(req: Request):
    results_df = find_vehicle(req.origin, req.prmpt)

    if results_df.empty:
        raise HTTPException(
            status_code=404,
            detail="No vehicles found matching your prompt within a 50km radius."
        )

    records = results_df.to_dict(orient="records")

    vehicle_list = [
        Vehicle(
            veh_id=row["vehicle_id"],
            brand=row["brand"],
            model=row["model"],
            add=row["address"]
        )
        for row in records
    ]

    return Response(vehicles=vehicle_list)