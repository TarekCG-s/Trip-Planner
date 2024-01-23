
# Trip Planner

## Overview
The Trip Planner is a small python project designed to organize a list of boarding cards, sort them and display a set of instructions to help following the plan. 

## Features
- **Sort Travel Destinations:** Takes a collection of boarding cards with different means of transportation and sorts them in the order of origin and destination.
- **Display Trip Plan:** Prints the instructions of the sorted plan, detailing each step of the trip.

## Installation

Python3 - no extra libraries are required.
## Usage

### Step 1: Importing the Module
First, ensure that the `TripPlanner` class and other required classes (`BoardingCard`, `Destination`, `Transportation`) are accessible in your Python environment.

```python
from trip_planner import TripPlanner
from boarding_card import BoardingCard
from transportations import FlightTransportation

```

### Step 2: Create Boarding Cards
Create instances of `BoardingCard` for each leg of the journey. Each `BoardingCard` should contain details about the departure and arrival destinations, along with transportation details.

```python
flight1 = FlightTransportation(
    "AD313", "27C", "15", "Baggage will be delivered in destination"
)
flight2 = FlightTransportation(
    "MD344", "17C", "5", "Baggage will be delivered in destination"
)


card1 = BoardingCard(from_destination="Dubai", to_destination="Istanbul", transportation_details=flight1)
card2 = BoardingCard(from_destination="London", to_destination="Dubai", transportation_details=flight2)

```

### Step 3: Initialize the Trip Planner
Pass the list of boarding cards to the `TripPlanner`.

```python
trip_planner = TripPlanner(boarding_cards=[card1, card2])
```

### Step 4: Display Trip Plan
Call the `display_trip_plan` method to output the sorted journey plan.

```python
trip_planner.display_trip_plan()
```
