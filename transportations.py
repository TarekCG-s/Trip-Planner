from abc import ABC, abstractmethod
from constants import TransportationTypes


class Transportation(ABC):
    transportation_type = None

    @abstractmethod
    def display_details(self, from_destination, to_destination) -> str:
        raise NotImplementedError


class TrainTransportation(Transportation):
    transportation_type = TransportationTypes.TRAIN.value

    def __init__(
        self,
        seat,
    ) -> None:
        self.seat = seat

    def display_details(self, from_destination: str, to_destination: str) -> str:
        return f"Take {self.transportation_type} from {from_destination} to {to_destination}. Sit in seat {self.seat}"


class BusTransportation(Transportation):
    transportation_type = TransportationTypes.BUS.value

    def __init__(
        self,
        seat=None,
    ) -> None:
        self.seat = seat

    def display_details(self, from_destination: str, to_destination: str) -> str:
        seat_details = f"Sit in seat {self.seat}" if self.seat else "No seat assignment"
        return f"Take the {self.transportation_type} from {from_destination} to {to_destination}. {seat_details}."


class FlightTransportation(Transportation):
    transportation_type = TransportationTypes.FLIGHT.value

    def __init__(
        self,
        flight_no: str,
        seat: str,
        gate: str,
        baggage_details: str = None,
    ) -> None:
        self.seat = seat
        self.flight_no = flight_no
        self.gate = gate
        self.baggage_details = baggage_details

    def display_details(self, from_destination: str, to_destination: str) -> str:
        msg = f"from {from_destination} airport take flight {self.flight_no} to {to_destination}. Gate {self.gate}, seat {self.seat}. "
        if self.baggage_details:
            msg += self.baggage_details

        return msg
