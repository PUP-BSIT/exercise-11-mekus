import emoji
import random

def say_hello(user_message):
    emoji_list = [":smile:", ":cry:", ":heart:", ":fire:", ":thumbs_up:"]
    
    chosen_emoji = random.choice(emoji_list)
    
    message = emoji.emojize(f"{user_message} {chosen_emoji}", language='alias')
    
    print(message)

def jundam_main():
    """Main function to run the banner display."""
    print("\n=== Jundam's Module ===\n")
    
    user_input = input("Enter your message: ")
    
    say_hello(user_input)