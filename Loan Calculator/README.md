# Loan Calculator

### About this project
Personal finances are an important part of life. Sometimes you need some extra money and decide to take a loan, or you want to buy a house using a mortgage. To make an informed decision, you need to be able to calculate different financial parameters. Let’s make a program that can help us with that!

### Learning Outcomes
You will practice using mathematics and Python in everyday tasks and learn how to use third-party modules and libraries. You will also learn more about different financial instruments.

### Run

Requirements:
- Python 3.9
`python loancalculator.py`

# Code it yourself:

## 1. Beginning

### Description

Let's think about what a loan calculator should be able to do. In general, it takes several parameters like a loan principal and interest, calculates the values the user wants to know (for example, monthly payment or overpayment), and outputs them to the user.

Not familiar with these concepts? Don't worry, we will explain them to you in simple terms. The principal is the original amount of money you borrow. The interest is a charge for borrowing that money, usually calculated as a percentage of the principal amount.

### Objective

Let's start by imitating this behavior. There are some prepared variables in the source code: these are text messages that our loan calculator can output. In this stage, all you need to do is output them in the right order.

### Example

Output:
```
Loan principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The loan has been repaid!
```

## 2. Dreamworld

### Description

If you found the previous stage too easy, let's add something interesting. The best loans are probably those with a 0% interest.

Let's make some calculations for 0% loan repayments. The user might know the period of the loan and want to calculate the monthly payment. Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full.

In this stage, we need to ask the user to input the loan principal amount. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.

Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:
```
payment = principal/months = 1000/9 = 111.11...
```
Of course, you can’t pay that amount of money. You have to round up this value and make it 112. Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:
```
last payment = principal−(periods−1)∗payment = 1000−8∗112 = 104
```
In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.

### Objective

The behavior of your program should look like this:

* Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
* To perform further calculations, you'll also have to ask for the required missing value.
* Finally, output the results for the user.


### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that this is not part of the input.

Example 1
```
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
> m
Enter the monthly payment:
> 150

It will take 7 months to repay the loan
```
Example 2
```
Enter the loan principal:
> 1000
What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
> m
Enter the monthly payment:
> 1000

It will take 1 month to repay the loan
```
Example 3
```
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 10

Your monthly payment = 100
```
Example 4
```
Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment
> p
Enter the number of months:
> 9

Your monthly payment = 112 and the last payment = 104.
```
