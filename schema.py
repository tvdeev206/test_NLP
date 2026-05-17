from pydantic import BaseModel
from typing import List

class Coordinates(BaseModel):
    lat: float
    lon: float

class Vehicle(BaseModel):
    veh_id: str
    brand: str
    model: str
    add: str

class prompt(BaseModel):
    prompt: str

class Request(BaseModel):
    origin: Coordinates
    prmpt: prompt

class Response(BaseModel):
    vehicles: List[Vehicle]



