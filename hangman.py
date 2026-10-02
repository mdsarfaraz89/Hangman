"""Text-based Hangman game.

CodeAlpha Python Programming Internship.
"""

import random

WORDS = ["python", "keyboard", "internet", "program", "variable"]
MAX_WRONG = 6

HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def choose_word(words=WORDS):
    """Pick a random word from the list."""
    return random.choice(words)


def mask_word(word, guessed):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def validate_guess(guess, guessed):
    """Return (is_valid, message). A guess must be a single, new letter."""
    if len(guess) != 1 or not guess.isalpha():
        return False, "Please enter a single letter."
    if guess in guessed:
        return False, "You already guessed that letter."
    return True, ""


def has_won(word, guessed):
    """True when every letter of the word has been guessed."""
    return all(letter in guessed for letter in word)


def play(word=None):
    """Run one round. Returns True if the player won."""
    word = word or choose_word()
    guessed = set()
    wrong = 0

    while wrong < MAX_WRONG:
        print(HANGMAN_STAGES[wrong])
        print("\nWord:", mask_word(word, guessed))
        print("Wrong guesses left:", MAX_WRONG - wrong)
        if guessed:
            print("Guessed:", " ".join(sorted(guessed)))

        guess = input("Guess a letter: ").strip().lower()
        valid, message = validate_guess(guess, guessed)
        if not valid:
            print(message)
            continue

        guessed.add(guess)
        if guess in word:
            print("Correct!")
            if has_won(word, guessed):
                print("\nYou won! The word was '" + word + "'.")
                return True
        else:
            wrong += 1
            print("Wrong!")

    print(HANGMAN_STAGES[MAX_WRONG])
    print("\nGame over! The word was '" + word + "'.")
    return False


def main():
    print("=== HANGMAN ===")
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
