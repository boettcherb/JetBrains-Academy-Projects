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

## 3. Predicting Future Input

### Description

Now we will start predicting the future user input. You will be surprised how often people repeat the same patterns!

Imagine the following: after the second stage for a string `0101010100101001010101000111101010010101010010101010101` we have calculated the amount of a certain character (0 or 1) that follows a specific triad of numbers: `'000': [0, 1], '001': [4, 1], '010': [5, 16], '011': [0, 1], '100': [1, 4], '101': [16, 0], '110': [0, 1], '111': [1, 1]`. Now, the user enters the sequence 001101. How can we foresee the next numbers?

Starting with the 4th character, we can predict the input based on the triads obtained in the previous stage. We've learned that the combination "001" (the first three characters) was followed by a "0" in 4 cases out of 5. So, the estimated probability that the user will enter "0" as the fourth character is 4/5 = 80%. For "1" probability is 1/5 = 20%. Therefore, we will choose "0'" as the fourth character. Similarly, the 5th character is predicted based on the statistics for the triad preceding it ("011"), and so on.

And what about the first three characters? For this task, you don't need to do this. Generate a sequence of three binary numbers, and that's it. Based on this triple, make predictions for further symbols. 

### Objective

In this stage, your program should:

1. Take and preprocess user input as described in stage 1.
2. Calculate user statistics using triads as described in stage 2 (but don't output the statistics this time).
3. Ask the user to enter another test string of 0's and 1's the values in which we will try to predict, and preprocess the new input.
4. Going through the string entered by the user, estimate the frequency of occurrence of "0" or "1" after each triad and generate predictions: if the count of 0's after the current triad is higher, the program should predict "0", otherwise, predict "1". If the counts are equal, the choice can be made in a random way.
5. The first three symbols may be predicted by chance one by one using the `random` module. You can also invent your own algorithm here, for instance, make use of the overall frequencies of 0's and 1's in the user input.
6. Test the accuracy of our predictor (excluding the first 3 randomly predicted symbols) by comparing the real input and the prediction. As the final output, print the line `Computer guessed right N out of M symbols (ACC%)`, where `N` is the number of correctly guessed symbols, `M` is the total length of the test input, and `ACC` is the accuracy value with 0.01% precision. Remember to exclude the first 3 symbols from the calculation!


### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
Print a random string containing 0 or 1:

> 0101001010010101011111100010010110000101010101010100101
The current data length is 63, 37 symbols left
Print a random string containing 0 or 1:

> 01010101001010010101010001111001010010101010010101010101

Final data string:
010100101001010101111110001001011000010101010101010010101010101001010010101010001111001010010101010010101010101


Please enter a test string containing 0 or 1:

0110001010100101
prediction:
1101011010101101

Computer guessed right 10 out of 13 symbols (76.92 %)
```

## 4. "Generate Randomness" Game

### Description

In the final stage, we will gather all our components to construct a game where you will try to beat the system created by your hands. Initially, the player has a virtual capital of $1000. Every time the computer guesses a symbol correctly, the player loses one dollar. Every time the system is wrong, the player gets one dollar.

### Objective

In this final stage, your program should:

1. Get and preprocess user input just like in stage 1.
2. Learn user patterns by collecting triad statistics like in stage 2.
3. Ask the user to enter test strings or type `enough` to exit the game. Each test string must be preprocessed (in order to leave only "0" and "1" symbols). After that, you should launch the prediction algorithm and calculate the number of correctly guessed symbols. After each iteration, you should show the player's balance with the message `Your capital is now $X`, where `X` is the player's virtual capital.
4. It would be great if you kept updating the system by allowing it to learn from the test data as well. However, this update should happen only after the prediction and the verification stages are done: let's be honest with the user.
5. Finish the game with the words `Game over!`.


### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
Please give AI some data to learn...
The current data length is 0, 100 symbols left
Print a random string containing 0 or 1:

> 010100100101010101000010001010101010100100100101001
The current data length is 63, 37 symbols left
Print a random string containing 0 or 1:

> 011010001011111100101010100011001010101010010001001010010011

Final data string:
010100100101010101000010001010101010100100100101001011010001011111100101010100011001010101010010001001010010011

You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!

Print a random string containing 0 or 1:
> 0111001001
prediction:
1000101011

Computer guessed right 4 out of 7 symbols (57.14 %)
Your capital is now $999

Print a random string containing 0 or 1:
> some wrong input

Print a random string containing 0 or 1:
> 0101001001
prediction:
0001011011

Computer guessed right 5 out of 7 symbols (71.43 %)
Your capital is now $996

Print a random string containing 0 or 1:
> enough
Game over!
```
