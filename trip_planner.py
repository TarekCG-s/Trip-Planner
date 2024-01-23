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
            from_destination = destinations.setdefault(card.from_destination, Destination(card.from_destination))
            to_destination = destinations.setdefault(card.to_destination, Destination(card.to_destination))
            
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

    def get_instructions_for_trip(self):
        destinations: List[Destination] = self.get_sorted_destinations()
        instructions = []
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
            instructions.append(f"{idx + 1}. {transportation_instructions}")
        return instructions

    def display_trip_instructions(self):
        instructions = self.get_instructions_for_trip()
        for line in instructions:
            print(line)
