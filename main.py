import modules

def display_menu():
    """Displays the main menu for the Mekus modules."""
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
        else:
            # If the choice is not valid, print an error message
            print("Invalid choice! Please select a number between 1 and 6.")
    except ValueError:
        # Handle the case where the input is not a number
        print("Invalid input! Please enter a number.")
    
    # Return None if the input is invalid
    return None

def handle_user_choice(choice):
    """Handles the user's choice and calls the corresponding module."""
    match choice:
        case 1:
            # TODO: Implement Agulto's module
            pass
        case 2:
            # TODO: Implement Dazo's module
            pass
        case 3:
            # TODO: Implement Jundam's module
            pass
        case 4:
            # TODO: Implement Olazo's module
            pass
        case 5:
            # TODO: Implement Serohijo's module
            pass

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