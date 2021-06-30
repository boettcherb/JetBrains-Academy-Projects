# Duplicate File Handler

### About this project
Duplicate File Handler is a useful tool that can free some space on your drive. Write a handler that checks and compares files in a folder, displays the result, and removes duplicates.

### Learning Outcomes
Learn how to work with files and folders. Get familiar with hashing, learn how to apply it to your tasks.

### Run

Requirements:
- Python 3.9
`python duplicatefilehandler.py`

# Code it yourself:

## 1. Here Come the Files

### Description

A computer is a great thing. It helps us store and manage tons of information. Every user knows how to work with folders. In this step, we will learn how to get a list of files and folders within a specific directory.

### Objectives

In this stage, your program should:

1. Accept a command-line argument that is a root directory with files and folders. Print `Directory is not specified` if there is no command-line argument;
2. Iterate over folders and print file names with their paths. The direction of the slashes in the printed out paths do not matter. Tests are platform independent, so different style of slashes ("/" or "\") are valid.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Example 1:
```
Suppose, you have the following set of files and folders:

+---[root_folder]
    |
    +---wall.png
    +---pass.txt
    +---[docs]
    |   |
    |   +---project.py
    |   +---calc.xls
    |   +---tutorial.mp4
    |   +---[res]
    |       |
    |       +---data.json
    |   +---[output]
    |       |
    |       +---result.json
    +---[masterpiece]
        |
        +---rick_astley_never_gonna_give_you_up.mp3
```
Program output:
```
> python handler.py root_folder

root_folder/wall.png
root_folder/pass.txt
root_folder/docs/project.py
root_folder/docs/calc.xls
root_folder/docs/tutorial.mp4
root_folder/docs/res/data.json
root_folder/docs/output/result.json
root_folder/masterpiece/rick_astley_never_gonna_give_you_up.mp3
```
