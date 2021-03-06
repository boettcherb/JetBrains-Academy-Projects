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

## 2. Multiplication by Number

### Description

In this stage, you are going to implement the multiplication of a matrix by a constant. To do this, you need to multiply every element of the matrix by that constant.

### Objectives

Write a program that:
1. reads a matrix and a constant,
2. outputs the result of their multiplication.

The first line of the input contains the number of rows and the number of columns of the matrix. The next lines contain rows of the matrix. The last line contains the constant.

The constant and the elements of the matrix are integers.

### Examples

Example 1:

Input:
```
3 3
1 2 3
4 5 6
7 8 9
3
```
Output:
```
3 6 9
12 15 18
21 24 27
```
Example 2:

Input:
```
2 3
1 2 3
4 5 6
0
```
Output:
```
0 0 0
0 0 0
```

## 3. Matrix by Matrix Multiplication

### Description

The next stage is the multiplication of matrices. This operation is a little more complex because it’s not enough to simply multiply the corresponding elements.

Unlike with addition, the sizes of the matrices can be different: the only restriction is that the number of columns in the first matrix should equal the number of rows for the second matrix. The multiplication of matrix A with n rows and m columns and matrix B with m rows and k columns is C = A x B. The resulting matrix has n rows and k columns, where every element is a sum of the multiplication of m elements across the rows of matrix A by m elements down the columns of matrix B.

Another really important thing is that A x B is not equal to B x A​. In fact, these are not even possible to multiply if k != i. If k = i, the resulting matrices would still be different.

### Objectives

In this stage, you should write a program that can do all operations on matrices that you've learned.

Write a program that does the following:

1. Prints a menu consisting of 4 options. The example shows what the menu should look like.
2. Reads the user's choice.
3. Reads all data (matrices, constants) needed to perform the chosen operation. The example shows the input format in each case.
4. Calculates the result and outputs it. The example shows how your output should look like.
5. Repeats all these steps.

The program should keep repeating this until the `"Exit"` option is chosen.

If some operation cannot be performed, output a warning message.

Also, you should support floating-point numbers.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 1
Enter size of first matrix: > 4 5
Enter first matrix:
> 1 2 3 4 5
> 3 2 3 2 1
> 8 0 9 9 1
> 1 3 4 5 6
Enter size of second matrix: > 4 5
Enter second matrix:
> 1 1 4 4 5
> 4 4 5 7 8
> 1 2 3 9 8
> 1 0 0 0 1
The result is:
2 3 7 8 10
7 6 8 9 9
9 2 12 18 9
2 3 4 5 7

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 2
Enter size of matrix: > 2 2
Enter matrix:
> 1.5 7.0
> 6.0 5.0
Enter constant: > 0.5
The result is:
0.75 3.5
3.0 2.5

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 3
Enter size of first matrix: > 3 3
Enter first matrix:
> 1 7 7
> 6 6 4
> 4 2 1
Enter size of second matrix: > 3 3
Enter second matrix:
> 3 2 4
> 5 5 9
> 8 0 10
The result is:
94 37 137
80 42 118
30 18 44

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 1
Enter size of first matrix: > 2 2
Enter first matrix:
> 1 2
> 3 2
Enter size of second matrix: > 1 1
Enter second matrix:
> 1
The operation cannot be performed.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: > 0
```

## 4. Transpose

### Description

In this stage, you should implement matrix transposition. Matrix transposition is an operation in linear algebra that replaces rows with columns and returns a new matrix as a result. This is an operation on just a single matrix.

The main diagonal of a matrix is a line with elements from a_1,1 to a_n,n. The side diagonal of a matrix is a line from a_1,n to a_n,1.

In math, there is only one type of matrix transposition: transposition along the main diagonal. In this stage, you should implement the other three types of transposition to practice your array skills. These four types are:

* transposition along the main diagonal
* transposition along the side diagonal
* transposition along the vertical line
* transposition along the horizontal line


### Objectives

In this stage, you should add an option to transpose matrices. If the user chooses this option, your program should provide them with 4 types of transposition and ask them to choose one. Then it should read the matrix, transpose it, and output the result. Refer to the example to see the exact format.

Note that your program should still be able to do all operations on matrices that you've implemented in the previous stage.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: > 4

1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: > 1
Enter matrix size: > 3 3
Enter matrix:
> 1 7 7
> 6 6 4
> 4 2 1
The result is:
1 6 4
7 6 2
7 4 1

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice: > 0
```

## 5. Determined!

### Description

In this stage, you should write a program that calculates a determinant of a matrix. You can check out some videos about linear algebra to understand the essence of the determinant and why it is important. To see how to calculate the determinant of any square matrix, watch a video about minors and cofactors and computing the n x n determinant.

A determinant is a single number that can be computed from the elements of a square matrix. There is a classical way to find the determinant of a matrix with an order less than 3.

A determinant of a 2-order matrix is equal to the difference between the product of elements on the main diagonal and the product of elements on the side diagonal. The determinant of a 1-order matrix is just the single element.

Now let's move on to the minor and the cofactor of a matrix. Minor(i,j) of a matrix is the determinant of the submatrix we get from the remaining elements after removing the i row and j column from this matrix.

Cofactor(i,j)​ of a matrix is the corresponding Minor(i,j) multiplied by (-1)^{i+j}. Notice that the cofactor is always preceded by a positive + or negative − sign.

We often need to find the determinant of a matrix of the order greater than 2. In this case, we have to use expansion by rows or columns where the determinant is equal to a sum of a single row or a single column multiplied by the cofactors of the elements in the corresponding row or column. To do this, you should use a recursive method.

### Objectives

In this stage, your program should support calculating the determinant of a matrix. Refer to the example to see how it should be implemented.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
Your choice: > 5
Enter matrix size: > 3 3
Enter matrix:
> 1 7 7
> 6 6 4
> 4 2 1
The result is:
-16

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
Your choice: > 5
Enter matrix size: > 5 5
Enter matrix:
> 1 2 3 4 5
> 4 5 6 4 3
> 0 0 0 1 5
> 1 3 9 8 7
> 5 8 4 7 11
The result is:
191

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
Your choice: > 0
```

## 6. Inverse Matrix

### Description

In this stage, you should find the inverse of a matrix. The inverse matrix A^{−1} is the matrix whose product with the original matrix A is equal to the identity matrix.

A x A^{-1} = I

The inverse of a matrix can be found using this formula:

A^{−1} = 1/det(A) x C^T

As you can see, it contains a lot of operations you implemented in the previous stages: finding cofactors of all the elements of the matrix, transposition of the matrix, finding the determinant of a matrix, and multiplication of a matrix by a constant.

det(A) is the determinant of matrix A, and C^T is the matrix consisting of cofactors of all elements of the matrix A transposed along the main diagonal. The inverse matrix can’t be found if det(A) equals zero.

### Objectives

In this stage, your program should support finding the inverse of a matrix. Refer to the example to see how it should be implemented.

Note that in some cases the inverse of a matrix does not exist. In such cases, your program should output a warning message.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > 6
Enter matrix size: > 3 3
Enter matrix:
> 2 -1 0
> 0 1 2
> 1 1 0
The result is:
 0.33   0  0.33
-0.33   0  0.66
 0.16 0.5 -0.33

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > 6
Enter matrix size: > 2 2
Enter matrix:
> 2 1
> 4 2
This matrix doesn't have an inverse.

1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > 0
```
