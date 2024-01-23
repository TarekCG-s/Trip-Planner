from transportations import Transportation

class Destination:
    def __init__(self, name, previous = None, next = None, transportation_details: Transportation = None) -> None:
        self.name = name
        self.previous: Destination = previous
        self.next: Destination = next
        self.transportation_details: Transportation = transportation_details

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
