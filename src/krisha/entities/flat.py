from dataclasses import dataclass


@dataclass
class Flat:
    id: int
    uuid: str
    url: str
    room: int
    square: int
    city: str
    lat: float
    lon: float
    description: str
    photo: str
    price: int
    star: int
    focus: int
