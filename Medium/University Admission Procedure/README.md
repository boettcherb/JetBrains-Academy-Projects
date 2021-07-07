# University Admission Procedure

### About this project
It takes a lot of hard work to enroll in the university of your dreams. Although, we tend to dismiss how difficult it is for the university to handle the document volume. In this project, you'll deal with university applicants. You'll implement an algorithm to determine which applicants are going to be enrolled. At each stage, the algorithm will gradually become more complex and comprehensive!

### Learning Outcomes
Practice loops and various mathematical operations. Learn how to handle files and different types of collections such as lists (including nested lists) and dictionaries. Put to use the sorting function and see how useful it can be.

### Run

Requirements:
- Python 3.9
`python universityadmissionprocedure.py`

# Code it yourself:

## 1. Mini-Calculator

### Description

Let's create a program that will help the university to determine the best candidates for enrolling!

The first step is very simple. An applicant needs to take three exams and submit the scores. The score of an exam can vary from 0 to 100. Your program should read the numbers representing the exam scores, calculate the mean exam score, and output it. And enroll the applicant to the university, as there are no other contestants yet.

### Objectives

At this stage, your program should:

1. Take three inputs as integer numbers. They are the exam results.
2. Calculate the mean score of all three numbers. If the mean is a fractional number, don't discard the fractional part.
3. Print the resulting number.
4. Print the `Congratulations, you are accepted!` line.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
> 75
> 90
> 68
77.66666666666667
Congratulations, you are accepted!
```

## 2. Raising the Bar

### Description

It'd be great if universities could enroll everybody, but it's not very realistic, is it? Let's refine our algorithm. In this stage we need to set a threshold of the mean score — if the mean score of the applicant is equal to or greater than 60.0, the program should notify the applicant about the acceptance to the university. Otherwise, inform them about the rejection.

### Objectives

At this stage, your program should:

1. Read the numbers and output the mean score, as in the previous stage.
2. If the mean score is equal to or greater than `60.0`, output the following message: `Congratulations, you are accepted!`
3. If the mean score is less than `60.0`, output the following message: `We regret to inform you that we will not be able to offer you admission.`

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Example 1: the applicant is enrolled
```
> 70
> 56
> 81
69.0
Congratulations, you are accepted!
```
Example 2: the applicant is rejected
```
> 100
> 43
> 27
56.666666666666664
We regret to inform you that we will not be able to offer you admission.
```
