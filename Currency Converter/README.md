# Currency Converter

### About this project
Want to convert one currency to another? You can go to your bank website and do the math by yourself. Or you can write a program to do it quickly and efficiently! The Currency Converter is a simple console program that calculates the amount of money you get by converting one currency to another.

### Learning Outcomes
You will learn many concepts of Python — basic types, variables, arithmetic operations, loops, and working with files. Get a taste of more advanced features — JSON format, caching, and how to work with the network. You will write a currency converter program that uses a third-party service.

### Run

Requirements:
- Python 3.9
`python currencyconverter.py`

# Code it yourself:

## 1. Cryptocurrencies are the New Black

### Description

Today we start our new project. It will be a simple currency converter. Every person sometimes needs to convert one currency to another. But we need to start easy, so for now, all you need to do is to print "Meet a conicoin!" Please, make sure that the output formatting of your program follows the example output formatting.

### Objective

Imagine that there is a cryptocurrency called conicoin ("coni" is just an anagram of the word "coin"). Greet conicoin as shown in the example below.

### Example

Output:
```
Meet a conicoin!
```

## 2. Talking Numbers

### Description

Holy moly! Suddenly you remember that back in 2008 you purchased several conicoins! Are you officially rich? Well, we need to find it out. You need to write a program that shows how much you can get after selling your conicoins. One conicoin is 100 dollars. Read your amount of the conicoins as the input, convert them into dollars, and output the result. Also, express your joy, it's important.

### Objective

Find out if you are rich.

1. Input the amount of your conicoins.
2. Calculate the number of dollars you receive after the conversion. 1 conicoin = 100 dollars, print the result as shown below.
3. Woohoo! You are rich!

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Output:
```
> 42
I have 42 conicoins.
42 conicoins cost 4200 dollars.
I am rich! Yippee!
```

## 3. More Interaction

### Description

We are going to make our program more complex. As you remember, the conicoin rate was fixed in the previous stage. But in the real world, things are different. It's time to write a program that takes your conicoins and an up-to-date conicoin exchange rate, then counts how many dollars you would get, and prints the result.

### Objective

1. Get the number of conicoins from the user input.
2. Get the exchange rate from the user input.
3. Calculate and print the result.

### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:
```
Please, enter the number of conicoins you have: > 13
Please, enter the exchange rate: > 2
The total amount of dollars: 26
```
Example 2:
```
Please, enter the number of conicoins you have: > 128
Please, enter the exchange rate: > 3.21
The total amount of dollars: 410.88
```

## 4. Going Global

### Description

You can convert your conicoins into dollars, cool. What if you want a different currency? What if you're going to Morocco tomorrow? You'll need some dirhams, that's for sure. We need to improve our converter.

Take the imaginary exchange rates below and modify your program to work with 5 different currencies:

* RUB – Russian Ruble; 1 conicoin = 2.98 RUB;
* ARS – Argentine Peso; 1 conicoin = 0.82 ARS;
* HNL – Honduran Lempira; 1 conicoin = 0.17 HNL;
* AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;
* MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.

Take the number of conicoins as the user input, сonvert it to the specified currencies, and round the result to two decimals using the Python built-in function. Notice that the input number can have a fractional part!

### Objective

1. Get the number of conicoins from user input.
2. Print how much you will get in all five currencies mentioned above.

### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
```
Be aware that the dictionary elements are unordered.
```
Example 1:
```
> 17
I will get 50.66 RUB from the sale of 17.0 conicoins.
I will get 13.94 ARS from the sale of 17.0 conicoins.
I will get 2.89 HNL from the sale of 17.0 conicoins.
I will get 33.36 AUD from the sale of 17.0 conicoins.
I will get 3.54 MAD from the sale of 17.0 conicoins.
```
Example 2:
```
> 3.5
I will get 10.43 RUB from the sale of 3.5 conicoins.
I will get 2.87 ARS from the sale of 3.5 conicoins.
I will get 0.6 HNL from the sale of 3.5 conicoins.
I will get 6.87 AUD from the sale of 3.5 conicoins.
I will get 0.73 MAD from the sale of 3.5 conicoins.
```
