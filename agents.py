from crewai import Agent
from textwrap import dedent
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools
from langchain.llms.base import LLM
from groq import Groq
import os
from typing import Optional, List, Any

""" Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal..
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal: Create a 7 day travel iternary with detailed per-day plans,
        including budget, packing suggestion, and safety tips.

Captain/Manager/Boss:
- Expert travel agent 

Employees/Experts to hire:
- City Selection Expert
- Local Tour Guide    
    
Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


class GroqLLM(LLM):
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any,
    ) -> str:
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800 
        )

        return response.choices[0].message.content or ""

    @property
    def _llm_type(self) -> str:
        return "groq"

class TravelAgents:
    def __init__(self):
        self.llm = GroqLLM()

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in Travel planning and logistics.
                             I have decades of experience travel iterneraries."""),
            goal=dedent(f"""Create a {7}-day travel itinerary with accurate, real-world places.
                            You MUST verify places using the search tool before including them.
                            Do NOT rely on assumptions."""),
            tools=[
                SearchTools.search_internet],
            verbose=False,
            llm=self.llm,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather, season, prices,
                        and travel iternary"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=False,
            llm=self.llm,
        )
        
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""Knowlegable local guide with extensive information
                             about the city , it's attraction and customs"""),
            goal=dedent(f"""Provide the best insights about the selected city"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=False,
            llm=self.llm,
        )
