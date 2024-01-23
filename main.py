from dataclasses import dataclass
from typing import List
from transportations import (
    Transportation,
    BusTransportation,
    FlightTransportation,
    TrainTransportation,
)
from boarding_card import BoardingCard
from trip_planner import TripPlanner


bus_transportation = BusTransportation()
train_transportation = TrainTransportation("10F")

flight_transportation1 = FlightTransportation(
    "MS788", "12A", "8", "Baggage will we automatically transferred from your last leg"
)

flight_transportation2 = FlightTransportation(
    "SK455", "23C", "89", "Baggage drop at ticket counter 344"
)


cards = [
    BoardingCard("Cairo", "Alexandria", bus_transportation),
    BoardingCard("Beirut", "Istanbul", flight_transportation1),
    BoardingCard("Alexandria", "Beirut", flight_transportation2),
    BoardingCard("Sohag", "Cairo", train_transportation),
]

trip_planner = TripPlanner(boarding_cards=cards)
trip_planner.display_trip_instructions()