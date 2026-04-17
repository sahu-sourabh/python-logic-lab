import random

def roll_dice_logic():
    """Generates and returns two random dice values."""
    return random.randint(1, 6), random.randint(1, 6)

def sanitize_input(user_input):
    """Clean user input for consistent comparisons."""
    return user_input.strip().lower()

def get_random_number(start, end):
    """Generates a random number in a given range."""
    return random.randint(start, end)