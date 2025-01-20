import random

# Hangman stages
stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# List of words
words = ['python', 'developer', 'hangman', 'programming', 'code']

def hangman():
    word = random.choice(words)  # Randomly select a word
    guessed_word = ['_'] * len(word)  # Hidden word representation
    attempts = len(stages) - 1  # Number of wrong guesses allowed
    guessed_letters = set()  # Track guessed letters

    print("Welcome to Hangman!")
    print("Guess the word:", ' '.join(guessed_word))

    while attempts > 0 and '_' in guessed_word:
        print(stages[len(stages) - 1 - attempts])  # Show current hangman stage
        print(f"\nWord: {' '.join(guessed_word)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Remaining attempts: {attempts}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

    # Game result
    if '_' not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print(stages[-1])  # Show the final hangman stage
        print("\nGame over! The word was:", word)

# Run the game
hangman()
