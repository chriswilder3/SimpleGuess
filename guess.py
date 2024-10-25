import random

def get_user_guess():
    """
    Prompts the user to enter a 3-digit guess and validates the input.
    Returns the guess as a list of characters if valid.
    """
    while True:
        guess = input("Enter your 3-digit guess: ")
        if len(guess) == 3 and guess.isdigit():
            return list(guess)
        print("Invalid input. Please enter exactly 3 digits.")

def generate_secret_code():
    """
    Generates a random 3-digit code as a list of unique characters from 0-9.
    Returns the code as a list of strings.
    """
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(secret_code, user_guess):
    """
    Compares the user's guess to the secret code and generates clues.
    - Returns "CODE CRACKED" if the guess is correct.
    - Returns a list of clues:
      - 'Match' for correct digit and position,
      - 'Close' for correct digit but wrong position,
      - 'Nope' if no digits match.
    """
    if user_guess == secret_code:
        return "CODE CRACKED"

    clues = []

    for index, digit in enumerate(user_guess):
        if digit == secret_code[index]:
            clues.append("Match")
        elif digit in secret_code:
            clues.append("Close")

    # Return 'Nope' if no clues were added
    return clues if clues else ["Nope"]

# Main Game Loop
print("Welcome to Code Breaker! Try to guess my 3-digit code.")

# Generate the secret code at the start of the game
secret_code = generate_secret_code()
print("A secret 3-digit code has been generated. Start guessing!")

# Initialize clue report for tracking the game state
clue_report = []

# Keep asking for guesses until the code is cracked
while clue_report != "CODE CRACKED":
    # Get user guess and generate clues
    user_guess = get_user_guess()
    clue_report = generate_clues(secret_code, user_guess)
    
    # Display clues to the user
    print("Result of your guess:")
    if clue_report == "CODE CRACKED":
        print("Congratulations! You've cracked the code!")
    else:
        for clue in clue_report:
            print(clue)
