"""
Custom Tools for Auto Insurance
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
import random


class MembershipInput(BaseModel):
    action: str = Field(..., description="create or lookup")
    member_id: str = Field(default="", description="Member ID for lookup")
    member_info: dict = Field(default_factory=dict, description="Info for creation")


class MembershipTool(BaseTool):
    name: str = "Membership Manager"
    description: str = "Creates new members or looks up existing member information"
    args_schema: Type[BaseModel] = MembershipInput

    def _run(self, action: str, member_id: str = "", member_info: dict = None) -> str:
        try:
            if action == "create":
                new_id = str(random.randint(10000000, 99999999))
                return f"New member created with ID: {new_id}\nMembership card will be mailed within 5-7 business days."

            elif action == "lookup":
                # Simulated lookup
                names = ["Tom", "Sarah", "Mike", "Lisa", "John"]
                name = random.choice(names)
                return f"Member {member_id}: {name}\nStatus: Active\nPolicy: Auto Insurance"

            return "Invalid action"
        except Exception as e:
            return f"Error with membership: {str(e)}"


class ClaimsTool(BaseTool):
    name: str = "Claims Processor"
    description: str = "Creates and manages insurance claims"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, claim_details: str = "") -> str:
        try:
            claim_id = f"CLM-{random.randint(100000, 999999)}"
            return f"""Claim created successfully.

Claim ID: {claim_id}
Status: Open
Next Steps: Claims adjuster will contact you within 1 hour
Expected Resolution: 3-5 business days

A rental vehicle has been arranged and will be available within 24 hours."""
        except Exception as e:
            return f"Error processing claim: {str(e)}"


class RoadsideAssistanceTool(BaseTool):
    name: str = "Roadside Assistance Dispatcher"
    description: str = "Dispatches roadside assistance services"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, service_type: str = "towing", location: str = "") -> str:
        try:
            request_id = f"RSA-{random.randint(10000, 99999)}"
            eta = random.randint(20, 60)
            companies = ["Roadside Rescue", "Quick Tow", "Emergency Auto Services", "Fast Response Towing"]
            company = random.choice(companies)

            return f"""Roadside assistance dispatched.

Request ID: {request_id}
Service: {service_type}
Location: {location}
Provider: {company}
ETA: {eta} minutes

You will receive a call from the provider shortly."""
        except Exception as e:
            return f"Error dispatching assistance: {str(e)}"


class RewardsTool(BaseTool):
    name: str = "Rewards Finder"
    description: str = "Finds nearby reward offers for members"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, location: str = "") -> str:
        try:
            rewards = [
                "• Coffee Haven - 20% off any drink",
                "• Auto Parts Plus - 15% off oil change",
                "• The Local Diner - Free appetizer with entree",
                "• Movie Palace - $5 off any ticket",
                "• Fitness First - Free 1-week trial membership"
            ]

            return f"""Rewards available near {location}:

{chr(10).join(random.sample(rewards, min(3, len(rewards))))}

Show your member ID to redeem these offers."""
        except Exception as e:
            return f"Error finding rewards: {str(e)}"
