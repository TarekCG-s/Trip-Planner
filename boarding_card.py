from dataclasses import dataclass

from transportations import Transportation


@dataclass
class BoardingCard:
    from_destination: str 
    destination: str
    transportation_details: Transportation
