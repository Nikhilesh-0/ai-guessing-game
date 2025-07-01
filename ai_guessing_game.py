# AI Guessing Game: Computer tries to guess the number you're thinking of (1–100)
import random 
import time

def guessing_game():
    """
    AI Guessing Game — Python
    Think of a number between 1 and 100, and the computer will try to guess it!
    This game adds a fun twist by combining randomness with binary search logic to surprise the player.
    Handles edge cases, user tricks.
    Instructions are provided as you play. Enjoy the game!
    Author: Nikhilesh Kumar
    Last Edited: 1 July 2025
    """

    # --- Game Setup ---

    print("Think of a number between 1 and 100. Don't tell me, just keep it in mind 🤫")
    time.sleep(1.5)
    print("I'll try to guess it!")
    time.sleep(1)
    print("When I make a guess, respond with:")
    print("  'c' if I'm correct")
    print("  'h' if your number is higher")
    print("  'l' if your number is lower\n")
    time.sleep(1.5)

    # Initial guess boundaries
    low = 1
    high = 100
    # Count how many guesses the computer takes
    attempts=0
    # Flag to determine whether last user input was valid
    valid_input = True
    # Flags and constants
    CORRECT = 'c'
    HIGHER = 'h'
    LOWER = 'l'
    exit_all = False # Master flag to break out of the loop
    # --- Main Game Loop ---
    while True:
        # Handle logic where boundaries are invalid (user lied / inconsistency)
        if high < low:
            print("Hmm... that doesn't add up. Are you messing with me? 😒 Let's start over.")
            exit_all = True
        # Handle case when only one number is left to guess
        if high == low:
            while True:
                user_input = input(f"Is your number {high}? (c/h/l): ").strip().lower() 
                if(user_input == CORRECT):
                    print(f"Yay! I guessed it in {attempts+1} attempts! 🎯\n")
                    exit_all = True
                    break
                elif user_input == HIGHER or user_input == LOWER:
                    print("Wait, that's not possible 🤨. Let's not mess with the rules. Let's start over.")
                    exit_all = True
                    break
                
                else:
                    print("Oops! Please enter a valid response: 'c', 'h', or 'l'.")
            
        if exit_all:
            break
        # --- Guess Generation ---
        if valid_input:
            if attempts > 0:
                print("Give me another shot... 🎯")
                time.sleep(.5)
            # Alternate between randomness and binary search:
            # On even attempts → pick a random number within range for surprise
            # On odd attempts  → use binary search midpoint for efficiency
            if attempts % 2 == 0:
                guess = random.randint(low,high)
            else:
                guess = (low+high)//2
            attempts += 1
            print("My guess is",guess)
            time.sleep(.5)
        # --- User Feedback and Guess Adjustment ---
        user_input = input("Was I right? (c for correct, h for higher, l for lower): ").strip().lower()
        # Validate input first
        if user_input in [CORRECT, HIGHER, LOWER]:
            valid_input = True
        else:
            valid_input = False  
        if user_input == CORRECT:
            if attempts == 1:
                print("No way! Got it on the first try?! I'm magical ✨")
                print("I guessed your number in 1 attempt.")
            else:
                print(f"I guessed your number in {attempts} attempts.\n")
            if attempts <6:
                print("I'm impressed with myself 😎\n")
            break
        # Adjust range based on user's feedback
        elif user_input == HIGHER:
            low = guess+1
        elif user_input == LOWER:
            high = guess-1
        else:
            print("Please respond with 'c' (correct), 'h' (higher), or 'l' (lower).")

if __name__ == "__main__":
    guessing_game()
