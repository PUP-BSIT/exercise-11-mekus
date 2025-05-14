import random
from art import tprint, art

# Define a tuple of symbol names that can be randomly selected and displayed
SYMBOLS = ('cat', 'butterfly', 'coffee', 'happy', 'fish', 'love')

def show_art_symbol(user_name):
    """Prints user's name in ASCII art and displays a random symbol."""
    
    # Print the user's name in large ASCII letters
    tprint(user_name)
    
    # Randomly choose one symbol from the SYMBOLS list
    chosen_symbol = random.choice(SYMBOLS)
    
    # Display the name of the chosen symbol
    print(f"\nHere's a random symbol for you: {chosen_symbol}")
    
    # Print the ASCII art of the chosen symbol
    print(art(chosen_symbol))
    
    # Friendly closing message
    print("\nKeep smiling and coding!")

def dazo_main():
    """Main function to run the ASCII art display."""
    
    print("\n=== Dazo's Module ===\n")  # Display program header
    
    # Keep prompting until the user enters a non-empty name
    while True:
        # Ask user for input and remove extra spaces
        user_input = input("Enter your name: ").strip()  
        
        if user_input:
            # Capitalize the first letter of the name and display the art
            show_art_symbol(user_input.capitalize())
            break  # Exit loop after valid input
        
        # Inform user that input was invalid
        print("Name cannot be empty. Please try again.")