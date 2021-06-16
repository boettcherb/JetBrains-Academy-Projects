# Dominoes

### About this project
Have you ever wanted to code a game where the computer is your enemy? Well, this little project allows you to do just that.
Take turns playing classic dominoes against your computer in a race to victory.
Learn, how artificial intelligence can make use of simple statistics to make educated decisions. This project is all about basic concepts, put them to practice by making a fun little game.

### Learning Outcomes
This project is all about basic concepts. You'll work with strings, tuples, lists, conditional statements, and more.

### Run

Requirements:
- Python 3.9
`python dominoes.py`

# Code it yourself:

## 1. Setting Up The Game
### Theory

Note:
Before you start this project, it's better to get familiar with the basic domino rules. Keep in mind that there are many versions of the game. The rules used in this particular project will be described as we go along.

As you might know, a domino is a playing piece that is characterized by the two numbers written on it. The numbers are integers and can range from 0 to 6. A single domino piece has no orientation, so, a full domino set (that includes all the possible pairs of numbers) will have 28 unique dominoes.

You may think that there should be 7*7=49 dominoes in total. However, this is not the case because the combinations like [1,2] and [2,1] are the same domino, not two separate ones.

### Description

To play domino, you need a full domino set and at least two players. In this project, the game is played by you and the computer.

At the beginning of the game, each player is handed 7 random domino pieces. The rest are used as stock (the extra pieces).

To start the game, players determine the starting piece. The player with the highest domino or the highest double ([6,6] or [5,5] for example) will donate that domino as a starting piece for the game. After doing so, their opponent will start the game by going first. If no one has a double domino, the pieces are reshuffled and redistributed.

"Status" is the player who is to make the next move 

### Objective


1. Generate a full domino set. Each domino is represented as a list of two numbers. A full domino set is a list of 28 unique dominoes.
2. Split the full domino set between the players and the stock by random. You should get three parts: Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).
3. Determine the starting piece and the first player. Modify the parts accordingly. You should get four parts with domino pieces and one string indicating the player that goes first: either `"player"` or `"computer"`.
```
    Stock pieces      # 14 domino elements
    Computer pieces   # 7 or 6 domino elements
    Player pieces     # 6 or 7 domino elements
    Domino snake      # 1 starting domino
    Status            # the player that goes first
```
If the starting piece cannot be determined (no one has a double domino), reshuffle, and redistribute the pieces (step 3). Finally, output all five variables.

### Example

Example 1

The player makes the first move.
```
Stock pieces: [[2, 5], [1, 2], [3, 6], [0, 0], [0, 2], [5, 6], [3, 5], [2, 4], [3, 4], [1, 5], [0, 4], [2, 6], [3, 3], [1, 1]]
Computer pieces: [[1, 4], [1, 3], [2, 3], [4, 5], [2, 2], [0, 3]]
Player pieces: [[0, 6], [5, 5], [4, 4], [4, 6], [0, 1], [0, 5], [1, 6]]
Domino snake: [[6, 6]]
Status: player
```

Example 2

The computer makes the first move.
```
Stock pieces: [[2, 6], [3, 4], [5, 6], [0, 5], [1, 2], [4, 6], [2, 3], [0, 6], [0, 0], [6, 6], [2, 4], [2, 2], [0, 1], [3, 3]]
Computer pieces: [[0, 2], [3, 6], [4, 4], [3, 5], [1, 5], [0, 3], [2, 5]]
player pieces: [[1, 3], [1, 4], [4, 5], [1, 6], [1, 1], [0, 4]]
Domino snake: [[5, 5]]
Status: computer
```

## 2. The Interface
### Description

A good game needs a good interface. In this stage, you will make your output user-friendly.

The player should be able to see the domino snake, the so-called playing field, and their own pieces. It's a good idea to enumerate these pieces because throughout the game the player will be selecting them to make a move.

Two things must remain hidden from the player: the stock pieces and the computer's pieces. The player should not be able to see them, only the number of pieces remaining.

### Objective

1. Print the header using seventy equal sign characters (=).
2. Print the number of dominoes remaining in the stock – Stock size: [number].
3. Print the number of dominoes the computer has – Computer pieces: [number].
4. Print the domino snake. At this stage, it consists of the only starting piece.
5. Print the player's pieces, Your pieces:, and then one piece per line, enumerated.
6. Print the status of the game. If `status = "computer"`, print `"Status: Computer is about to make a move. Press Enter to continue..."`. If `status = "player"`, print `"Status: It's your turn to make a move. Enter your command."`. Note that both these statuses suppose that the next move will be made, but at this stage, the program should stop here. We will implement other statuses (like "win", "lose", and "draw") in the stages to come.

### Example

Example 1

The player makes the first move (status = "player")
```
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
```

Example 2

The Computer makes the first move (status = "computer")
```
======================================================================
Stock size: 14
Computer pieces: 7

[5, 5]

Your pieces:
1:[1, 3]
2:[1, 4]
3:[4, 5]
4:[1, 6]
5:[1, 1]
6:[0, 4]

Status: Computer is about to make a move. Press Enter to continue...
```

## 3. Taking Turns
### Description

It's time to bring the game to life. In this stage, you need to add a game loop that will allow players to take turns until the end-game condition is met.

In dominoes, you can make a move by taking one of the following actions:

* Select a domino and place it on the right side of the snake.
* Select a domino and place it on the left side of the snake.
* Take an extra piece from the stock (if it's not empty) and skip a turn.

To make a move, the player has to specify the action they want to take. In this project, the actions are represented by integer numbers in the following manner: `{side_of_the_snake (+/-), domino_number (integer)}` or `{0}`. For example:
* -6 : Take the sixth domino and place it on the left side of the snake.
* 6 : Take the sixth domino and place it on the right side of the snake.
* 0 : Take an extra piece from the stock (if it's not empty) and skip a turn.

When it's time for the player to make a move, your program must prompt the user for a number. If this number exceeds the limitations (larger than the number of dominoes), your program must generate an error message and prompt for input again. Once the valid input is received, your program must apply the move.

For now, don't bother about the AI, our goal is just to make the game playable. So, when it's time for the computer to make a move, make it choose a random number between `-computer_size` and `computer_size` (where the `computer_size` is the number of dominoes the computer has).

The end-game condition can be achieved in two ways:

1. One of the players runs out of pieces. The first player to do so is considered a winner.

2. The numbers on the ends of the snake are identical and appear within the snake 8 times. For example, the snake bellow will satisfy this condition:
```
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,6],[6,5]
```
These two snakes, however, will not:
```
[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5]
```
```
[6,5],[5,5],[5,2],[2,1],[1,5],[5,4],[4,0],[0,5],[5,3],[3,1]
```
If this condition is satisfied, it is no longer possible to go on with this snake. Even after emptying the stock, no player will have the necessary piece. Essentially, the game has come to a permanent stop, so we have a draw.

When the game ends, your program should print the result.

Throughout the gameplay, the snake will grow in length. If it gets too large, the interface might get ugly. To avoid this problem, draw only the first and the last three pieces of the snake, separate them by three dots, ..., for example, `[3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4]`.

### Objective

Modify your Stage 2 code:

1. At the end of the game, print one of the following phrases: `Status: The game is over. You won!`, `Status: The game is over. The computer won!`, or `Status: The game is over. It's a draw!`.
2. Print only the first and the last three pieces of the domino snake separated by three dots if it exceeds six dominoes in length.
3. Add a game loop that will repeat the following steps until the game ends:
* Display the current playing field (stage 2).
* If it's a user's turn, prompt the user for a move and apply it. If the input is invalid (a not-integer or it exceeds limitations), request a new input with the following message: `Invalid input. Please try again..`.
* If it's a computer's turn, prompt the user to press Enter, randomly generate a move, and apply it.
* Switch turns.

Keep in mind that at this stage we have no rules! Both the player and the computer can place their dominoes however they like.

### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

Typical gameplay.
```
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[4, 6]
5:[0, 1]
6:[0, 5]
7:[1, 6]

Status: It's your turn to make a move. Enter your command.
> 4
======================================================================
Stock size: 14
Computer pieces: 6

[6, 6][4, 6]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: Computer is about to make a move. Press Enter to continue...
>
======================================================================
Stock size: 14
Computer pieces: 5

[6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]
6:[1, 6]

Status: It's your turn to make a move. Enter your command.
> -6
======================================================================
Stock size: 14
Computer pieces: 5

[1, 6][6, 6][4, 6][1, 3]

Your pieces:
1:[0, 6]
2:[5, 5]
3:[4, 4]
4:[0, 1]
5:[0, 5]

Status: Computer is about to make a move. Press Enter to continue...
>
```
Example 2

Invalid input.
```
======================================================================
Stock size: 14
Computer pieces: 5

[4, 4][2, 3][3, 4]

Your pieces:
1:[1, 2]
2:[2, 6]
3:[0, 4]
4:[5, 6]
5:[2, 5]
6:[2, 4]

Status: It's your turn to make a move. Enter your command.
> Hello
Invalid input. Please try again.
>
```
Example 3

Mid-game example. The "domino snake" exceeds six dominoes in length.
```
======================================================================
Stock size: 7
Computer pieces: 4

[6, 6][6, 3][3, 0]...[4, 2][2, 3][3, 6]

Your pieces:
1:[0, 0]
2:[1, 2]
3:[5, 5]

Status: It's your turn to make a move. Enter your command.
```
Example 4

The player wins.
```
======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[3, 6][0, 3][3, 4]

Your pieces:
1:[4, 4]

Status: It's your turn to make a move. Enter your command.
> 1
======================================================================
Stock size: 13
Computer pieces: 2

[3, 5][2, 2][6, 6]...[0, 3][3, 4][4, 4]

Your pieces:

Status: The game is over. You won!
```
