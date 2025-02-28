from smolagents import CodeAgent, tool, HfApiModel
import numpy as numpy
import time
import datetime

# Tool to suggest a menu based on the occasion
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."
        
# Tool to calculate the time needed for the party
@tool
def calculate_party_time(tasks: list) -> str:
    """
    Calculates the total preparation time for the party.
    Args:
        tasks: A list of tasks with their respective time estimates.
    """
    total_time = sum(duration for task, duration in tasks)
    return f"Total preparation time: {total_time} minutes."

# Alfred, the butler, preparing the menu for the party
agent = CodeAgent(tools=[suggest_menu, calculate_party_time], model=HfApiModel())

# Preparing the menu for the party
agent.run( """
    Alfred needs to prepare for the party. Here are the tasks:
    1. Prepare the drinks - 30 minutes
    2. Decorate the mansion - 60 minutes
    3. Set up the menu - 45 minutes
    4. Prepare the music and playlist - 45 minutes

    If we start right now, at what time will the party be ready?
    """
          )
