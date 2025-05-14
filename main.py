import os
import modules

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_menu():
    """Displays the main menu for the Mekus modules."""
    clear_screen()  # Clear the screen before showing the menu
    print(
        "\n === Mekus Module Menu ==="
        "\n [1] Agulto's Module"
        "\n [2] Dazo's Module"
        "\n [3] Jundam's Module"
        "\n [4] Olazo's Module"
        "\n [5] Serohijo's Module"
        "\n [6] Exit"
    )

def get_user_choice():
    """Prompts the user for a choice and returns it."""
    try:
        # Prompt the user to enter a choice
        choice = int(input("Select a module (1-6): "))
        
        # Check if the choice is valid
        if 1 <= choice <= 6:
            return choice  # Return the valid choice
        
        # If the choice is not valid, print an error message
        print("Invalid choice! Please select a number between 1 and 6.")
        input("Press Enter to try again...")  # Wait before clearing screen
        
    except ValueError:
        # Handle the case where the input is not a number
        print("Invalid input! Please enter a number.")
        input("Press Enter to try again...")  # Wait before clearing screen
        
    # Return None if the input is invalid
    return None

def handle_user_choice(choice):
    """Handles the user's choice and calls the corresponding module."""
    clear_screen()  # Clear the screen before running the module
    match choice:
        case 1:
            modules.agulto_main()
        case 2:
            modules.dazo_main()
        case 3:
            modules.jundam_main()
        case 4:
            modules.olazo_main()  
        case 5:
            modules.serohijos_main()
    # Wait before returning
    input("\nPress Enter to return to the main menu...") 
     
def main():
    """Main function to run the Mekus modules."""
    while True:
        # Display the menu and get user choice
        display_menu()
        
        # Get the user's choice
        choice = get_user_choice()
        
        # If the choice is None (invalid), continue to the next iteration
        if choice is None:
            continue
        
        # If the choice is 6, exit the program
        if choice == 6:
            print("Exiting the program. Goodbye!")
            break
        
        # Handle the user's choice
        handle_user_choice(choice)

main()