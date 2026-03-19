from crewai import Task
from textwrap import dedent


""""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
-Develop a detailed itinerary, including city selection, attractions, and practical travel ad

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
        - A detailed 7 day travel iternary.
        
2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
        - Iternary Planner: Develop a detailed plan for each day day of the trip
        - City Selection: Analyze and pick the best cities.
        - Local Tour Guide: Find a local expert to provide insights and recommendation.
        
3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.


4. Task Description Template:
-Use this template as a guide to define each task in your CrewAl application.
-This template helps ensure that each task is clearly defined, actionable, and aligned with

Template:
---------
def [task_name) (self, agent, [parameters]):
    return Task(description=dedent(f'""
    **Task**: [Provide a concise name or summary of the task.]
    **Description**: [Detailed description of what the agent is expected to do, including actionable steps expected outcomes.This should be clear and direct, outlining the specific actions required to complete the task.]

    **Parameters**:
    --[Parameter1]: [Description]
    --[Parameter2]: [Description]
    ... [Add more parameters as needed.]
    
**Note**: [Optional section for incentives or encouragment for high quality work. This can include tips. ]    
    '''),(agent=agent)

"""
class TravelTasks:
    def _tip_section(self):
        return "Do your BEST WORK!"

    def plan_iternary(self, agent, cities, date_range, interests):
        return Task(
            description=dedent(f"""
                Create a {date_range}-day itinerary for {cities}. Interests: {interests}.

                Format EXACTLY like this:

                DAY 1:
                - Morning: activity
                - Afternoon: activity
                - Evening: activity

                DAY 2:
                - Morning: activity
                - Afternoon: activity
                - Evening: activity

                (continue for all {date_range} days)

                HOTELS:
                - Name | Location | Price

                RESTAURANTS:
                - Name | Cuisine | Price

                BUDGET:
                - Accommodation: amount
                - Food: amount
                - Transport: amount
                - Total: amount

                PACKING LIST:
                - item

                SAFETY TIPS:
                - tip
            """),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(f"""
                Recommend the best city to visit.
                Origin: {origin}, City: {cities}
                Interests: {interests}, Days: {travel_dates}

                Format:
                - Best City: name
                - Why: one sentence
                - Best Season: months
                - Daily Budget: amount
            """),
            agent=agent,
        )

    def gather_city_info(self, agent, city, interests, travel_dates):
        return Task(
            description=dedent(f"""
                Write a short city guide for {city}. Interests: {interests}.

                Format EXACTLY:

                CITY OVERVIEW:
                2 sentences about the city.

                TOP ATTRACTIONS:
                - Attraction | Why visit

                LOCAL CUSTOMS:
                - tip

                BEST TIME TO VISIT:
                - best months

                WEATHER:
                - weather during {travel_dates}

                COST OVERVIEW:
                - Budget per day: amount
            """),
            agent=agent,
        )