import emoji
import random

# A tuple of emoji names choose from
EMOJI_TUPLE = (":smile:", ":cry:", ":heart:", ":fire:", ":thumbs_up:")

def say_hello(user_message):
    """Picks a random emoji and adds it to the user's message."""
    
    chosen_emoji = random.choice(EMOJI_TUPLE)
    
    message = emoji.emojize(f"{user_message} {chosen_emoji}", language='alias')
    
    print(message)

def jundam_main():
    """Main function to run the banner display."""
    print("\n=== Jundam's Module ===\n")
    
    user_input = input("Enter your message: ")
    
    say_hello(user_input)