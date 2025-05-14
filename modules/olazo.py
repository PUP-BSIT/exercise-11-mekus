import random
import pyfiglet as pf
from termcolor import colored

# Initialize constant font and colors
FONT = "larry3d" 
COLORS = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

def display_banner(user_input):
    """Displays a banner with a greeting and a user-provided name."""
    
    # Create the banner using pyfiglet
    banner = pf.figlet_format(f"Hello {user_input}!", font=FONT)
    
    # Randomly select a color for the banner
    colored_banner = colored(banner, random.choice(COLORS))
    
    # Print the colored banner
    print(f"\n{colored_banner}")
    
def input_name():
    """Prompts the user for their name and returns it."""
    while True:
        # Prompt the user for their name
        user_input = input("Enter a name: ").strip()
        
        # Check if the input is not empty
        if user_input:
            return user_input.capitalize()  # Return the capitalized name
        
        # Print an error message if the input is empty
        print("Name cannot be empty! Please try again.")

def olazo_main():
    """Main function to run the banner display."""
    print("\n=== Olazo's Module ===\n")
    
    # Get user input
    user_input = input_name()
    
    # Display the banner with the user's name
    display_banner(user_input)