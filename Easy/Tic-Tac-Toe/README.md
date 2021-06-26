# Tic-Tac-Toe

### About this project
Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. Let’s program Tic-Tac-Toe and get playing!

### Learning Outcomes
After finishing this project, you'll get to know a lot about planning and developing a complex program from scratch, using functions, handling errors, and processing user input.

### Run

Requirements:
- Python 3.9
`python tictactoe.py`

# Code it yourself:

## 1. Welcome to the Battlefield!

### Description

Tic-tac-toe is known all over the world. Each country may have its own version of the name, sometimes the rules are different, but the essence of the game remains the same. Below are the main rules that may be familiar to you since childhood.

Tic-tac-toe is a game played by two players on a 3x3 grid. One of the players is 'X', and the other player is 'O'. X plays first, then O takes the next turn, and so on.

The players write 'X' and 'O' on a 3x3 field.

The first player that puts 3 X's or 3 O's in a straight line (including diagonals) wins the game.

### Objective

Your first task in this project is to print the game grid in the console output. Use what you’ve learned about the print() function to print three lines, each containing three characters (X’s and O’s) to represent a game of tic-tac-toe where all fields of the grid have been filled in. 

### Example

The example below shows how your output might look:
```
X O X
O X O
X X O 
```

## 2. The User is the Gamemaster

### Description

Our program should be able to display the grid at all stages of the game. Now we’re going to write a program that allows the user to enter a string representing the game state and correctly prints the 3x3 game grid based on this input. We’ll also add some boundaries around the game grid.

### Objective

In this stage, you will write a program that:

1. Reads a string of 9 symbols from the input and displays them to the user in a 3x3 grid. The grid can contain only `X`, `O` and `_` symbols.
2. Outputs a line of dashes `---------` above and below the grid, adds a pipe | symbol to the beginning and end of each line of the grid, and adds a space between all characters in the grid.

### Example

Examples below show how your output should look.
Notice that after `Enter cells:` comes the user input.

Example 1:
```
Enter cells: O_OXXO_XX
---------
| O _ O |
| X X O |
| _ X X |
---------
```
Example 2:
```
Enter cells: OXO__X_OX
---------
| O X O |
| _ _ X |
| _ O X |
---------
```
Example 3:
```
Enter cells: _XO__X___
---------
| _ X O |
| _ _ X |
| _ _ _ |
---------
```

## 3. What's up on the Field?

### Description

In this stage, we’re going to analyze the game state to determine if either player has already won the game or it is still ongoing, if the game is a draw, or if the user has entered an impossible game state (two winners, or with one player having made too many moves).

### Objective

In this stage, your program should:

1. Take a string entered by the user and print the game grid as in the previous stage.
2. Analyze the game state and print the result. Possible states:

* `Game` not finished when neither side has three in a row but the grid still has empty cells.
* `Draw` when no side has a three in a row and the grid has no empty cells.
* `X wins` when the grid has three X’s in a row.
* `O wins` when the grid has three O’s in a row.
* `Impossible` when the grid has three X’s in a row as well as three O’s in a row, or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).

In this stage, we will assume that either X or O can start the game.

You can choose whether to use a space or underscore to print empty cells.

### Examples

The examples below show outputs and analysis results for different game states. Your program should work in the same way.

Notice that after `Enter cells:` comes the user input.

Example 1:
```
Enter cells: XXXOO__O_
---------
| X X X |
| O O _ |
| _ O _ |
---------
X wins
```
Example 2:
```
Enter cells: XOXOXOXXO
---------
| X O X |
| O X O |
| X X O |
---------
X wins
```
Example 3:
```
Enter cells: XOOOXOXXO
---------
| X O O |
| O X O |
| X X O |
---------
O wins
```
Example 4:
```
Enter cells: XOXOOXXXO
---------
| X O X |
| O O X |
| X X O |
---------
Draw
```
Example 5:
```
Enter cells: XO_OOX_X_
---------
| X O   |
| O O X |
|   X   |
---------
Game not finished
```
Example 6:
```
Enter cells: XO_XO_XOX
---------
| X O _ |
| X O _ |
| X O X |
---------
Impossible
```
Example 7:
```
Enter cells: _O_X__X_X
---------
|   O   |
| X     |
| X   X |
---------
Impossible
```
Example 8:
```
Enter cells: _OOOO_X_X
---------
|   O O |
| O O   |
| X   X |
---------
Impossible
```

## 4. First Move!

### Description

It’s time to make our game interactive! Now we’re going to add the ability for a user to make a move.

To do this, we need to divide the grid into cells.

Suppose the top left cell has the coordinates (1, 1) and the bottom right cell has the coordinates (3, 3) like in this table:

(1, 1) (1, 2) (1, 3)
(2, 1) (2, 2) (2, 3)
(3, 1) (3, 2) (3, 3)

The program should ask the user to enter the coordinates of the cell where they want to make a move.

In this stage, the user plays as X, not O. Keep in mind that the first coordinate goes from left to right and the second coordinate goes from top to bottom. Also note that coordinates start with 1 and can be 1, 2, or 3.

What happens if the user enters incorrect coordinates? The user could enter symbols instead of numbers, or enter coordinates representing occupied cells or cells that aren’t even on the grid. You need to check the user's input and catch possible exceptions.

### Objective

The program should work as follows:

1. Get the 3x3 grid from the input as in the previous stages.
2. Output this 3x3 grid as in the previous stages.
3. Prompt the user to make a move.
4. The user should input 2 numbers that represent the cell where they want to place their X. (the 9 symbols representing the field will be the first line of input, and the 2 coordinate numbers will be the second line of input)
5. Analyze user input and show messages in the following situations:
    `This cell is occupied! Choose another one!` if the cell is not empty.
    `You should enter numbers!` if the user enters non-numeric symbols in the coordinates input.
    `Coordinates should be from 1 to 3!` if the user enters coordinates outside the game grid.
6. Update the grid to include the user's move and print the updated grid to the console.

The program should also check the user’s input. If the input is unsuitable, the program should tell the user why their input was wrong, and prompt them to enter coordinates again.

To summarize, you need to output the game grid based on the first line of input, and then ask the user to enter a move. Keep asking until the user enters coordinates that represent an empty cell on the grid, update the grid to include that move, and then output it to the console. You should output the field only 2 times: once before the user’s move, and once after the user has entered a legal move.

Do not delete the code you already wrote that analyzes the game state; you will need it in the final step of this project.

The project was changed. Now the coordinates start from the upper left corner. Look closely at the examples.

### Examples

The examples below show how your program should work.

Notice that after `Enter cells:` and `Enter the coordinates:` comes the user input.

Example 1:
```
Enter cells: X_X_O____
---------
| X   X |
|   O   |
|       |
---------
Enter the coordinates: 3 1
---------
| X   X |
|   O   |
| X     |
---------
```
Example 2:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```
Example 3:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 3 3
---------
|   X X |
| O O   |
| O X X |
---------
```
Example 4:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 2 3
---------
|   X X |
| O O X |
| O X   |
---------
```
Example 5:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 3 1
This cell is occupied! Choose another one!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```
Example 6:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: one
You should enter numbers!
Enter the coordinates: one one
You should enter numbers!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```
Example 7:
```
Enter cells: _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: 4 1
Coordinates should be from 1 to 3!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| X X X |
| O O   |
| O X   |
---------
```

## 5. Fight!

### Description

Our game is almost ready! Now let's combine what we’ve learned in the previous stages to make a game of tic-tac-toe that two players can play from the beginning (with an empty grid) through to the end (until there is a draw, or one of the players wins).

The first player has to play as X and their opponent plays as O.

### Objective

In this stage, you should write a program that:

1. Prints an empty grid at the beginning of the game.
2. Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a grid with the changes if everything is okay.
3. Ends the game when someone wins or there is a draw.

You need to output the final result at the end of the game.

Good luck!

The project was changed. Now the coordinates start from the upper left corner. Look closely at the examples.

### Example

The example below shows how your program should work.
Notice that after `Enter the coordinates:` comes the user input.
```
---------
|       |
|       |
|       |
---------
Enter the coordinates: 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: 2 2
This cell is occupied! Choose another one!
Enter the coordinates: two two
You should enter numbers!
Enter the coordinates: 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: 1 1
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: 3 3
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: 2 1
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: 3 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: 2 3
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: 3 2
---------
| O     |
| O X O |
| X X X |
---------
X wins
```
