# Hangman

### About this project
Hangman is a popular yet grim puzzle game. A cruel computer hides a word from you, which you try to guess letter by letter. If you fail, you'll be “hanged”. If you win, you'll survive. You’ve probably played the game at least once or twice. Now you can actually create this game yourself!

### Learning Outcomes
With functions, loops, lists and other variables, this is a great project for Python basics. As a cherry on top, it even includes a random module. Don’t be intimidated by the number of stages; they ensure that your dive into Python is safe and smooth.

### Run

Requirements:
- Python 3.9
`python hangman.py`

# Code it yourself:

## 1. Hello, Hangman

### Description

Hangman is a popular yet grim intellectual game. A cruel computer hides a word from you. Letter by letter you try to guess it. If you fail, you'll be hanged, if you win, you'll survive. See also: Wikipedia

You probably played the game at least once in your life; now you can actually create this game yourself!

Let's look at a brief overview of what you are going to build in this project. Here is what the gameplay should look like:

1. In the main menu, a player can choose to either play or exit the game.
2. If the user chooses to play, the computer picks a word from a list: this will be the answer to the puzzle.
3. The computer asks the player to enter a letter that they think is in the word.
4. If that letter does not appear in the word and this letter hasn't already been guessed, the computer counts it as a miss. A player can only afford 8 misses before the game is over.
5. If the letter does occur in the word, the computer notifies the player. If there are letters left to guess, the computer invites the player to go on.
6. When the entire word is uncovered, it's a victory! The game calculates the final score and returns to the main menu.

This may sound complex, but the project is split into small stages with hints to see you through. The final product is sure to be replayable and quite engaging!

Let's start with an announcement that will greet the player. You already know how to print something using Python. Try to apply that knowledge to entice your friends to play with an announcement for your game!

### Objective

In this stage, you should write a program that prints the lines shown in the example below.

### Example

Output:
```
H A N G M A N
The game will be available soon.
```

## 2. Let's play a game

### Description

At this stage, you will create a real game, though it will still be quite simple. There will be two possible outcomes. Let's first print a welcome message and then ask the player to guess the word we set for the game. If our player manages to guess the exact word, the game reports "win"; otherwise it will "hang" the player.

### Objective

1. Ask the player for a possible word.
2. Print You survived! if the user guesses the word.
3. Print You lost! if the user guesses incorrectly.

By the way, python should be the word the player needs to guess to win the game.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not the part of the output.

Example 1
```
H A N G M A N
Guess the word: > python
You survived!
```
Example 2
```
H A N G M A N
Guess the word: > java
You lost!
```
