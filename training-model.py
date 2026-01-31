# Import necessary modules
from smolagents import tool
from smolagents.models import TransformersModel
from datetime import datetime, timedelta


# Define tools for the party planning model
# Tools: suggest_menu, parse_tasks, calculate_party_time, calculate_finish_time
@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggest a menu based on the occasion.

    Args:
        occasion (str): Type of occasion.

    Returns:
        str: Suggested menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "Three-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "High-energy buffet with healthy options."
    return "Custom menu."


@tool
def parse_tasks(_: str) -> list:
    """
    Return predefined preparation tasks and durations.

    Args:
        _ (str): Ignored input.

    Returns:
        list: List of (task, duration_minutes).
    """
    return [
        ("Prepare drinks", 30),
        ("Decorate mansion", 60),
        ("Set up menu", 45),
        ("Prepare music and playlist", 45),
    ]


@tool
def calculate_party_time(tasks: list) -> int:
    """
    Calculate total preparation time.

    Args:
        tasks (list): List of (task, duration).

    Returns:
        int: Total duration in minutes.
    """
    return sum(duration for _, duration in tasks)


@tool
def calculate_finish_time(start_time: str, total_minutes: int) -> str:
    """
    Calculate finish time from a start time and duration.

    Args:
        start_time (str): Start time in HH:MM format.
        total_minutes (int): Duration in minutes.

    Returns:
        str: Finish time in HH:MM format.
    """
    start = datetime.strptime(start_time, "%H:%M")
    finish = start + timedelta(minutes=total_minutes)
    return finish.strftime("%H:%M")



# Example usage of the tools
# Get tasks and calculate total preparation time
tasks = parse_tasks("")
total_minutes = calculate_party_time(tasks)
# Calculate finish time from current time
now = datetime.now().strftime("%H:%M")
finish_time = calculate_finish_time(now, total_minutes)
# Print finish time
print(f"Party will be ready at {finish_time}")



# Generate a polite explanation using a language model
model = TransformersModel(model_id="YOUR_MODEL_ID_HERE")
response = model.generate_text(
    f"The party will be ready at {finish_time}. Explain politely as a butler."
)

print(response)

