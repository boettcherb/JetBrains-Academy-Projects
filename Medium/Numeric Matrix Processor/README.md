# Numeric Matrix Processor

### About this project
Here’s a project for devoted matrix enthusiasts: learn to perform a variety of operations on matrices including addition, multiplication, finding the determinant, and dealing with inverse matrices. If you are working on your tech or math major, this project is a good chance for you to learn matrices in action and not just in your notebook.

### Learning Outcomes
Apart from learning a whole lot about matrices, you will become familiar with the Math library, recursion, and the many ways of using nested lists in practice.

### Run

Requirements:
- Python 3.9
`python numericmatrixprocessor.py`

# Code it yourself:

## 1. Mini-Calculator

### Description

Matrices have a wide range of applications in programming: they're used for digital image processing, graph representation and algorithms on a graph, graphic effects, applied math, statistics, and much more.

Since matrices are tables of numbers, they are usually presented in code as 2D-arrays. In this project, you will learn how to read and output matrices, do operations on them, and compute the determinant of a square matrix. At first, you will work with matrices with integer elements, and later the elements will be floating-point numbers.

Let’s start with matrix addition.

For two matrices to be added, they must have an equal number of rows and columns. The sum of matrices A and B will be a matrix with the same number of rows and columns as A or B. The sum of A and B, denoted A + B or B + A, is computed by adding the corresponding elements of A and B.

### Objectives

In this stage, you should write a program that:

1. Reads matrix A from the input.
2. Reads matrix B from the input.
3. Outputs their sum if it is possible to add them. Otherwise, it should output the `ERROR` message.

Each matrix in the input is given in the following way: the first line contains the number of rows n and the number of columns m. Then n lines follow, each containing m integers representing one row of the matrix.

Output the result in the same way but don't print the dimensions of the matrix.

### Examples

Example 1:

Input:
```
4 5
1 2 3 4 5
3 2 3 2 1
8 0 9 9 1
1 3 4 5 6
4 5
1 1 4 4 5
4 4 5 7 8
1 2 3 9 8
1 0 0 0 1
```
Output:
```
2 3 7 8 10
7 6 8 9 9
9 2 12 18 9
2 3 4 5 7
```
Example 2:

Input:
```
2 3
1 4 5
4 5 5
4 5
0 1 0 4 5
1 7 8 9 4
1 2 3 5 6
1 3 4 3 8
```
Output:
```
ERROR
```
