# CodeAlpha_Hangman

A simple console Hangman game: guess the word one letter at a time before the drawing is complete.

> Built for the **CodeAlpha Python Programming Internship**.

## Features
- 5 predefined words, chosen at random
- 6 incorrect guesses allowed, with an ASCII hangman drawing
- Input validation (single letters only, no repeats)
- Play-again option
- Unit tests for the game logic

## Concepts used
- `random`
- `while` loops with `break` / `continue`
- `if` / `elif` / `else`
- Strings, lists and sets
- Functions and docstrings
- `unittest`

## Project structure
```
CodeAlpha_Hangman/
+-- hangman.py        # the game
+-- test_hangman.py   # unit tests
+-- Hangman.ipynb     # step-by-step notebook
+-- README.md
+-- requirements.txt
+-- .gitignore
```

## How to run
Requires Python 3.8+ (no external libraries).

```bash
python hangman.py
```

Run the unit tests:
```bash
python -m unittest -v
```

Open the step-by-step notebook:
```bash
pip install jupyter
jupyter notebook
```

## Sample run
```
=== HANGMAN ===

  +---+
  |   |
      |
      |
      |
      |
=========

Word: _ _ _ _ _ _
Wrong guesses left: 6
Guess a letter: p
Correct!
```

## Future improvements
- Load words from a file
- Add difficulty levels
- Add a hint option
- Track win/loss score

## Author
Your Name - [LinkedIn](https://linkedin.com/in/your-profile) - [GitHub](https://github.com/your-username)
