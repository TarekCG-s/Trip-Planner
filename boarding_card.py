from dataclasses import dataclass

from transportations import Transportation


@dataclass
class BoardingCard:
    from_destination: str 
    to_destination: str
    transportation_details: Transportation
