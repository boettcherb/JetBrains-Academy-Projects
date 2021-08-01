# Memorization Tool

### About this project
It would be great to remember anything at any time. Alas, our mental capacity is limited. The good thing is that there are a lot of tools to help us memorize things. In this project, we are going to create a tool for memorizing lines, poems, speeches, and other text-based materials.

### Learning Outcomes
Work with the SQLAlchemy ORM and an SQLite database to create a tool for memorizing. Practice loops, lists, and various string methods.

### Run

Requirements:
- Python 3.9
`python memorizationtool.py`

# Code it yourself:

## 1. Make Your Own Flashcards

### Description

A good memorizing tool can boost your short and long-term memory. If you tried to learn a foreign language, you probably know what a flashcard is. It is an excellent device to remember facts. Flashcards alone are not enough, we need a special technique.

Let's create our flashcards first. A flashcard is a piece of paper with a question on one side and the answer on the other. Let's assume we need to memorize the capital cities of various countries. Write the country name on one side and the capital on the other.

### Objectives

In this stage, we need to create our first flashcards.
When the program starts, it should print the menu below. It is our main menu (1):
```
1. Add flashcards
2. Practice flashcards
3. Exit
```
If `1` is entered, the program should print the following sub-menu (2):
```
1. Add a new flashcard
2. Exit
```
By choosing the `Add a new flashcard` option, a user is prompted to enter a `Question` and an `Answer`. Once they are entered, the program automatically returns to the sub-menu (2). Iterate this process every time a user wants to add a new flashcard.

**Flashcard practice:**

The `Practice flashcards` option in the main menu (1) should print all the questions and answers that have been added previously. If there are no flashcards, print `There is no flashcard to practice!` and return to the main menu (1).

Your flashcard should appear on the screen in the following way:
```
Question: {your question}
Please press "y" to see the answer or press "n" to skip:
```
If `y` is entered, the program should output `Answer: {your answer}` and go to the next flashcard. If there are no flashcards to show, return to the main menu (1).

If `n` is entered, skip to the next flashcard. If there are no flashcards to show, return to the main menu (1).

Once the program has reached the end of a flashcard list, return to the main menu (1).

Please keep in mind the following:

- In case of the wrong input, output the following message: `{wrong key} is not an option`. Wait for the right input.
- Your questions and answers must be non-empty values. Otherwise, wait for the input.
- Don't forget about the goodbye message. Output `Bye!` every time a user exits the program.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Example 1:
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 2

There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Brazil?
Answer:
> Brasilia

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Lebanon?
Answer:
> Beirut

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Brazil?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Brasilia

Question: What is the capital city of Lebanon?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Beirut

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital city of Montenegro?
Answer:
> Podgorica

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital city of Brazil?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Brasilia

Question: What is the capital city of Lebanon?
Please press "y" to see the answer or press "n" to skip:
> n


Question: What is the capital city of Montenegro?
Please press "y" to see the answer or press "n" to skip:
> y

Answer: Podgorica

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```
Example 2:
```
1. Add flashcards
2. Practice flashcards
3. Exit
> 5

5 is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> we

we is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 1

1. Add a new flashcard
2. Exit
> 3

3 is not an option

1. Add a new flashcard
2. Exit
> 0w

0w is not an option

1. Add a new flashcard
2. Exit
> 1

Question:
>
Question:
>
Question:
> What is the capital city of Japan?
Answer:
>

Answer:
>

Answer:
> Tokyo

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
```