# Hangman Game

Welcome to the Hangman game, a simple text-based implementation of the classic Hangman game in Python.

## Description

The Hangman game allows players to guess a secret word letter by letter. For each incorrect guess, a part of the "hangman" figure is drawn. The player wins by guessing all the letters in the word before the hangman figure is complete, and loses if the hangman figure is completed before guessing all the letters.

## Requirements

1. Python 3
2. Pygame library (for playing sounds)

## Installation

1. Clone or download the repository.

2. Install the Pygame library using pip:

```
pip install pygame
```

## How to Play

1. Run the game by executing the `main.py` file:

```
python main.py
```

2. When the game starts, it will display the Hangman figure with some dashes representing the letters of the word to be guessed.

3. The game will prompt you to guess a letter from the provided keyboard layout.

4. If your guessed letter is present in the word, the corresponding dash will be replaced with the letter.

5. If your guessed letter is not in the word, the Hangman figure will be drawn step by step, and you will lose a life.

6. Continue guessing letters until you either guess the entire word correctly or run out of lives.

7. The game will announce the final results - whether you won or lost, along with your score.

## Additional Features

1. The game includes different word categories, such as "food," "place," "animals," etc.

2. The game has background music for both success and failure cases.

3. The Hangman figure changes based on the number of lives remaining.

## Customize the Word List

You can customize the list of words in the `word_list` variable inside the `Hangman` class constructor (`__init__`). Simply modify the tuples to add or change the word and its associated category.

## Contributing

If you would like to contribute to the project, feel free to submit pull requests or open issues.


Enjoy the game and have fun playing Hangman! 🎮
