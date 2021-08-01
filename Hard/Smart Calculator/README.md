# Smart Calculator

### About this project
Calculators are a very helpful tool that we all use on a regular basis. Why not create one yourself, and make it really special? In this project, you will write a calculator that not only adds, subtracts, and multiplies, but is also smart enough to remember your previous calculations.

### Learning Outcomes
Apart from writing a useful program (everyone uses calculators!), you will learn a lot about lists, strings and dictionaries. You will also get closer experience with 2 important data structures: the stack and the queue.

### Run

Requirements:
- Python 3.9
`python smartcalculator.py`

# Code it yourself:

## 1. 2+2

### Description

Your task is to make a smart calculator. What do you usually expect from a calculator? Of course, it is bound to support 4 basic operations: multiplication, division, addition, and subtraction. But we don't stop there and add the ability to calculate expressions containing parenthesis and the ability to remember the previous result. This will be a console application, which you will improve gradually, from simple to complex.
So, the first version of the calculator will only support the addition operation for two numbers. In this version, you will not receive the plus symbol (+) as an input, you will accept this as an unwritten rule (because only one operation is supported).

### Objectives

Write a program that reads two integer numbers from the same line and prints their sum in the standard output. Numbers can be positive, negative, or zero.

### Example

The example below shows the input and the corresponding output. Your program should work in the same way. Do not add extra characters after the output!

The greater-than symbol followed by a space (`> `) represents the user input. Notice that it's not the part of the input.
```
> 5 8
13
```

## 2. 2+2+

### Description

It is high time to improve the previous version of the calculator. What if we have many pairs of numbers, the sum of which we need to find? It will be very inconvenient to run the program every time. So then let's add a loop to continuously calculate the sum of two numbers. Be sure to have a safeword to break the loop. Also, It would be nice to think through situations where users enter only one number or do not enter numbers at all.

### Objectives

1. Write a program that reads two numbers in a loop and prints the sum in the standard output.
2. If a user enters only a single number, the program should print the same number. If a user enters an empty line, the program should ignore it.
3. When the command `/exit` is entered, the program must print `"Bye!"` (without quotes), and then stop.

### Example

The greater-than symbol followed by a space (`> `) represents the user input.
```
> 17 9
26
> -2 5
3

> 7
7
> /exit
Bye!
```

## 3. Count Them All

### Description

In rare cases, we need to calculate the sum of only two numbers. Now it is time to teach the calculator to read an unlimited sequence of numbers. Also, let's take care of ourselves if after a while we want to remember what our program does. For this purpose, we'll introduce a new command `/help` to our calculator. Users who have first exposure to this program may use `/help` as well to know more about it!

### Objectives

- Add to the calculator the ability to read an unlimited sequence of numbers.
- Add a `/help` command to print some information about the program.
- If you encounter an empty line, do not output anything.

### Example

The greater-than symbol followed by a space (`>  `) represents the user input.
```
> 4 5 -2 3
10
> 4 7
11
> 6
6
> /help
The program calculates the sum of numbers
> /exit
Bye!
```

## 4. Add Subtractions

### Description

Finally, we got to the next operation: subtraction. It means that from now on the program must receive the addition `+` and subtraction `-` operators as an input to distinguish operations from each other. It must support both unary and binary minus operators. Moreover, If the user has entered several same operators following each other, the program still should work (like Java or Python REPL). Also, as you remember from school math, two adjacent minus signs turn into a plus. The smart calculator ought to have such a feature.

Pay attention to the `/help` command, it is important to maintain its relevance depending on the changes (in the next stages too). You can write information about your program in free form, but the main thing is that it should be understandable to you and other users.

### Objectives

- The program must calculate expressions like these: `4 + 6 - 8`, `2 - 3 - 4`, and so on.
- Modify the result of the `/help` command to explain these operations.
- Decompose your program using functions to make it easy to understand and edit later.
- The program should not stop until the user enters the `/exit` command.
- If you encounter an empty line, do not output anything.

### Example

The greater-than symbol followed by a space (`> `) represents the user input.
```
> 8
8
> -2 + 4 - 5 + 6
3
> 9 +++ 10 -- 8
27
> 3 --- 5
-2
> 14       -   12
2
> /exit
Bye!
```
