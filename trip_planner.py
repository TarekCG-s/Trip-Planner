from typing import List

from transportations import Transportation
from boarding_card import BoardingCard
from destination import Destination


class TripPlanner:
    def __init__(self, boarding_cards: List[BoardingCard]):
        self.boarding_cards = boarding_cards
        self.__destinations = self.__get_list_of_destinations()
        self.__first_destination = self.__get_first_destination(
            destinations=self.__destinations
        )

    def __get_list_of_destinations(self) -> List[Destination]:
        destinations = {}
        for card in self.boarding_cards:
            from_destination_name = card.from_destination
            to_destination_name = card.to_destination

            from_destination = destinations.get(from_destination_name)
            to_destination = destinations.get(to_destination_name)
            if not from_destination:
                from_destination = Destination(from_destination_name)
                destinations[from_destination_name] = from_destination

            if not to_destination:
                to_destination = Destination(to_destination_name)

                destinations[to_destination_name] = to_destination

            from_destination.next = to_destination
            from_destination.transportation_details = card.transportation_details
            to_destination.previous = from_destination

        return list(destinations.values())

    def __get_first_destination(self, destinations: List[Destination]) -> Destination:
        first_destination = None
        for destination in destinations:
            if not destination.previous:
                first_destination = destination

        return first_destination

    def get_sorted_destinations(self) -> List[Destination]:
        sorted_destinations = []
        destination = self.__first_destination
        while destination:
            sorted_destinations.append(destination)
            destination = destination.next

        return sorted_destinations

    def display_trip_plan(self):
        destinations: List[Destination] = self.get_sorted_destinations()
        for idx, destination in enumerate(destinations):
            transportation_instructions = ""
            if destination.transportation_details:
                transportation_instructions = (
                    destination.transportation_details.display_details(
                        destination.name, destination.next.name
                    )
                )
            else:
                transportation_instructions = (
                    "You have arrived at your final destination."
                )
            print(f"{idx + 1}. {transportation_instructions}")
