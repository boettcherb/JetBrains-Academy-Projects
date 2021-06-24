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

## 3. Make your choice

### Description

If there is a predefined word, the game isn't replayable. You already know the word, so there’s no longer any challenge. At this stage, let's make the game more challenging by choosing a word from a special list with a variety of options. This way, our game will have more replay value.

### Objective

1. Create the following list of words: 'python', 'java', 'kotlin', 'javascript'.
2. Program the game to choose a word from the list at random. You can enter more words, but let's stick to these four for now.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the output.

Example 1. The computer randomly chose `python` from the list.
```
H A N G M A N
Guess the word: > python
You survived!
```
Example 2. The computer randomly chose something other than `python` from the list.
```
H A N G M A N
Guess the word: > python
You lost!
```
Example 3. The computer randomly chose something other than `kotlin` from the list.
```
H A N G M A N
Guess the word: > kotlin
You lost!
```

## 4. Help is on the Way

### Description

Now our game has become quite hard, and your chances of guessing the word depend on the size of the list. When the list has four words, you only have a 25% chance to guess correctly. So let's show a little mercy to the player and add a hint for them.

### Objective

1. As in the previous stage, you should use the following word list: 'python', 'java', 'kotlin', 'javascript'
2. Once the computer has chosen a word from the list, show its first 3 letters. Hidden letters should be replaced with hyphens ("-").

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the output.

Example 1
```
H A N G M A N
Guess the word jav-: > java
You survived!
```
Example 2
```
H A N G M A N
Guess the word pyt---: > pythia
You lost!
```

## 4. Help is on the Way

### Description

Let's make the game iterative. Now it's time to make the game resemble the classic version of Hangman a bit more. The player should now guess letters in the word instead of typing the entire word all at once. If the player guesses a letter, it should be uncovered in the word. For now, start by building the defeat condition and add 8 tries to guess a letter that appears in the word. When the player runs out of attempts, the game ends.

Later we will determine the winning conditions, but in this stage, let's just see how well our player guesses the word on each attempt.

### Objective

Now your game should work as follows:

1. A player has exactly 8 tries and enters letters. Nothing changes if a player has more tries left but they have already guessed the word.
2. If the letter doesn't appear in the word, the computer takes one try away – even if the user has already guessed this letter.
3. If the player doesn't have any more attempts, the game should end and the program should show a losing message. Otherwise, the player can continue to input letters.
4. Also, the word should be selected from our list: `'python', 'java', 'kotlin', 'javascript'`, so that your program can be tested more reliably.

Please, make sure that your program's output formatting precisely follows the example. Pay attention to the empty lines between tries and at the end.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the output.

Example 1
```
H A N G M A N

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
That letter doesn't appear in the word

-a-a---i--
Input a letter: > z
That letter doesn't appear in the word

-a-a---i--
Input a letter: > l
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > p

-a-a---ip-
Input a letter: > h
That letter doesn't appear in the word

-a-a---ip-
Input a letter: > k
That letter doesn't appear in the word

Thanks for playing!
We'll see how well you did in the next stage
```
Example 2
```
H A N G M A N

----
Input a letter: > j

j---
Input a letter: > i
That letter doesn't appear in the word

j---
Input a letter: > g
That letter doesn't appear in the word

j---
Input a letter: > o
That letter doesn't appear in the word

j---
Input a letter: > a

ja-a
Input a letter: > v

java
Input a letter: > a

java
Input a letter: > j

Thanks for playing!
We'll see how well you did in the next stage
```
