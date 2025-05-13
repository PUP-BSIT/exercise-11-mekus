import random
import pyfiglet as pf
from termcolor import colored

FONT = "larry3d" 
COLORS = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

def display_banner(user_input):
    """Displays a banner with a greeting and a user-provided name."""
    
    # Create the banner using pyfiglet
    banner = pf.figlet_format(f"Hello {user_input}!", font=FONT)
    
    colored_banner = colored(banner, random.choice(COLORS))
    
    print(f"\n{colored_banner}")
    
def input_name():
    """Prompts the user for their name and returns it."""
    while True:
        user_input = input("Enter a name: ").strip()
        if user_input:
            return user_input.capitalize()
        
        print("Name cannot be empty! Please try again.")

def olazo_main():
    """Main function to run the banner display."""
    print("\n=== Olazo's Module ===\n")
    
    user_input = input_name()
    display_banner(user_input)