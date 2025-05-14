import random
import time
from colorama import Fore, Style, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Constants
WORKOUT_COUNT = 5

# Define the workout categories and exercises
WORKOUT_CATEGORIES = {
    'strength': [
        "Push-ups", "Pull-ups", "Squats", "Lunges", "Deadlifts", "Bench Press"
    ],
    'cardio': [
        "Running", "Cycling", "Jump Rope", "Swimming", "Rowing", "HIIT"
    ],
    'flexibility': [
        "Yoga", "Stretching", "Pilates", "Foam Rolling", "Tai Chi"
    ],
    'all': [
        "Push-ups", "Pull-ups", "Squats", "Lunges", "Deadlifts", "Bench Press",
        "Running", "Cycling", "Jump Rope", "Swimming", "Rowing", "HIIT",
        "Yoga", "Stretching", "Pilates", "Foam Rolling", "Tai Chi"
    ]
}

def get_workout(user_input):
    """Generate and print a workout based on the user input."""
    # If no valid input, select a random category
    if user_input not in WORKOUT_CATEGORIES:
        user_input = random.choice(list(WORKOUT_CATEGORIES.keys()))
        print(f"{Fore.RED}Invalid or empty input.Random category")

    # Randomly select workouts from the chosen category
    workout = random.sample(WORKOUT_CATEGORIES[user_input], WORKOUT_COUNT)  

    print(f"\n{Fore.CYAN}Here's your workout for today:{Style.RESET_ALL}")
    for exercise in workout:
        print(f"{Fore.GREEN}- {exercise}{Style.RESET_ALL}")
        time.sleep(1)  # Add a 1-second delay between each exercise

def agulto_main():
    """Main function to run the banner display."""
    print("\n=== Agulto's Module ===\n")
    ascii_banner = pyfiglet.figlet_format("Agulto's Workout")
    print(Fore.MAGENTA + ascii_banner)  # Color the banner in magenta
    
    user_input = input(f"{Fore.WHITE}Enter a workout category "
                       "(strength, cardio, flexibility, all) "
                       "or press Enter for a random category: ").strip().lower()
    
    get_workout(user_input)

