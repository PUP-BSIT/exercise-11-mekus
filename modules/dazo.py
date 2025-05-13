import random
from art import tprint, art

SYMBOLS = ('cat', 'butterfly', 'coffee', 'happy', 'fish', 'love')

def show_art_symbol(user_name):
    """Prints user's name in ASCII art and displays a random symbol."""
    tprint(user_name)

    chosen_symbol = random.choice(SYMBOLS)
    print(f"\nHere's a random symbol for you: {chosen_symbol}")
    print(art(chosen_symbol))

    print("\nKeep smiling and coding!")

def dazo_main():
    """Main function to run the ASCII art display."""
    print("\n=== Dazo's Module ===\n")

    while True:
        user_input = input("Enter your name: ").strip()
        if user_input:
            show_art_symbol(user_input.capitalize())
            break
        print("Name cannot be empty. Please try again.")