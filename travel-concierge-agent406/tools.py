"""Custom Tools for Travel Concierge Agent"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class DestinationResearchInput(BaseModel):
    interests: str = Field(..., description="Travel interests and preferences")


class DestinationResearchTool(BaseTool):
    name: str = "Destination Research Tool"
    description: str = "Researches travel destinations based on interests, budget, and timing"
    args_schema: Type[BaseModel] = DestinationResearchInput

    def _run(self, interests: str) -> str:
        return f"Destination research for: {interests}\nNote: Integrate with travel APIs for real data"


class FlightSearchInput(BaseModel):
    destination: str = Field(..., description="Destination to search flights for")


class FlightSearchTool(BaseTool):
    name: str = "Flight Search Tool"
    description: str = "Searches for flight options and prices"
    args_schema: Type[BaseModel] = FlightSearchInput

    def _run(self, destination: str) -> str:
        return f"Flight search for {destination}\nNote: Integrate with flight APIs (Skyscanner, Amadeus)"


class HotelSearchInput(BaseModel):
    location: str = Field(..., description="Location to search hotels")


class HotelSearchTool(BaseTool):
    name: str = "Hotel Search Tool"
    description: str = "Searches for accommodation options"
    args_schema: Type[BaseModel] = HotelSearchInput

    def _run(self, location: str) -> str:
        return f"Hotel search for {location}\nNote: Integrate with Booking.com, Expedia APIs"


class ItineraryBuilderInput(BaseModel):
    destination: str = Field(..., description="Destination for itinerary")


class ItineraryBuilderTool(BaseTool):
    name: str = "Itinerary Builder Tool"
    description: str = "Builds detailed travel itineraries"
    args_schema: Type[BaseModel] = ItineraryBuilderInput

    def _run(self, destination: str) -> str:
        return f"Building itinerary for {destination}\nNote: Include activities, dining, logistics"
