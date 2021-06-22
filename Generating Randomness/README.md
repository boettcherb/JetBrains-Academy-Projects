# Generating Randomness

### About this project
Everyone knows that people are bad at generating random things. In this project, we will check this assumption using a small program that will predict "random" user actions. We'll see if you can beat it!

### Learning Outcomes
In addition to raising the metaphysical question of free will, this project will teach you to work with dictionaries and lists, as well as with simple predictive models.

### Run

Requirements:
- Python 3.9
`python generatingrandomness.py`

# Code it yourself:

## 1. Input Processing

### Description

In order to train the machine to predict the next user input, we need to collect data about the user. We will ask them to press 0's and 1's on the keyboard in an unpredictable order. These data will be kept in a string of the format "011100101010...". All other characters should not be taken into account (in case the user makes a mistake and presses "2" instead of "1", for example).

### Objective

In this stage, your program should:

1. Set the minimal length of the string of zeros and ones that the user should enter. Let's choose the value 100: this will allow you to collect enough statistics without taking too much of the user's time.
2. Filter out inappropriate symbols from each user input.
3. Append the processed string to the general string containing all the data from the input.
4. Keep asking the user for new input strings and appending them to the general string until the length of the general string is equal or exceeds 100. If it exceeds 100, don't remove extra symbols: 100 symbols are the minimum required length, but the more data we have, the better.
5. Output the final data string.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

For simplicity, we will limit ourselves to a string of length 20 in this example.
```
Print a random string containing 0 or 1:

> 01000111001
Current data length is 11, 9 symbols left
Print a random string containing 0 or 1:

> 2345
Current data length is 11, 9 symbols left
Print a random string containing 0 or 1:

> 1010456
Current data length is 15, 5 symbols left
Print a random string containing 0 or 1:

> 0100010

Final data string:
0100011100110100100010
```

## 2. Analyzing User Input

### Description

Now it's time to reveal the secret of our magical predictive system. We will create a "profile" of the user that will contain information about patterns found in their "random" clicks. To do this, we will count how many times a certain character (0 or 1) follows a specific triad of numbers (for example, 000 or 011). For example, in the string "00010000", the triad "000" is once followed by a "0" and once by "1".

In the next stage, we will create a prediction algorithm based on this information.

### Objective

In this stage, your program should:

1. Read the user input the same way it did in the previous stage.
2. Output the result in the following format: triad: counts of 0, counts of 1, for example, 000: 57,12. The result for each triad should be printed on a new line. The triads must be ordered in ascending order of their decimal representation (for example, 110 in binary = 1*4+1*2+0*1 = 6 in decimal).

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
Print a random string containing 0 or 1:

> 01010010010001010100100101001001
The current data length is 32, 68 symbols left
Print a random string containing 0 or 1:

> 10100011001010101010111101001001011010
The current data length is 70, 30 symbols left
Print a random string containing 0 or 1:

> 0101101010100110101010101010001110011

Final data string:
01010010010001010100100101001001101000110010101010101111010010010110100101101010100110101010101010001110011

000: 0,3
001: 10,5
010: 13,18
011: 5,2
100: 3,12
101: 20,3
110: 2,5
111: 2,1
```
