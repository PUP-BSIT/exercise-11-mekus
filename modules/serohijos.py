import pyjokes
import random

# List of valid joke types that can be requested
VALID_JOKE_TYPES = ('neutral', 'chuck', 'all')

# Default joke type to use when no input is provided
DEFAULT_JOKE_TYPE = 'all'

def get_joke(joke_type=DEFAULT_JOKE_TYPE):
    # Check if the provided joke type is valid
    if joke_type not in VALID_JOKE_TYPES:
        # If not valid, randomly select a valid joke type
        joke_type = random.choice(VALID_JOKE_TYPES)
        print(f"Invalid type. Using random type: {joke_type}")

    # Return a joke from pyjokes using the specified (or corrected) type
    return pyjokes.get_joke(language='en', category=joke_type)

def display_menu():
    # Show menu options to the user
    print("\nOptions:")
    print("1. Get a neutral joke")
    print("2. Get a Chuck Norris joke")
    print("3. Get any joke")
    print("4. Exit")

def handle_user_choice(choice):
    # Execute action based on user input
    match choice:
        case "1":
            print(f"\n{get_joke('neutral')}")
        case "2":
            print(f"\n{get_joke('chuck')}")
        case "3":
            print(f"\n{get_joke('all')}")
        case _:
            print("Invalid choice. Please try again.")

def serohijos_main():
    # Main program loop
    print("\n=== Serohijos's Module ===")

    while True:
        display_menu()  # Show options
        user_choice = input("Enter your choice (1-4): ")  
        
        if user_choice == "4":
            print("Exiting the program...")
            break
        
        handle_user_choice(user_choice)  # Act on choice
        