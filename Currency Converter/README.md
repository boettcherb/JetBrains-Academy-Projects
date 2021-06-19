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

## 5. JSON and the Rates

### Description

In the previous stages, we worked with different real-world currencies but the exchange rates were fixed. Unfortunately (or not, depending on your political stance), we don't really have fixed exchange rates in today's world. At this stage, you will have to work with the Internet to get the information! The FloatRates site contains a special JSON page for each currency. Your task is to make requests to these pages and download the actual data on the exchange rates of the US dollar and the euro. Remember, that the data is stored in JSON format.

### Objective

There are many currency codes, for example, RUB, ARS, HNL, AUD, MAD, etc. Choose the one you like best and return the information about the exchange rates from the site specified above for only two currencies: USD and EUR.

1. Select one currency code, take it as the user input.
2. Make a request to `http://www.floatrates.com/daily/YOUR_CURRENCY_CODE.json`. Don't forget that you need to put the code in lowercase.
3. Print your result for USD and EUR.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
Be aware that the dictionary elements are unordered. The results of your output may differ, as the service updates the data once in twelve hours. Don't hesitate to print the whole string for your own interest, but it is not a part of the stage.
```
The output for HNL:
```
> HNL
{'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 0.040212252288502, 'date': 'Sun, 5 Jul 2020 12:00:01 GMT', 'inverseRate': 24.868042526579}
{'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 0.035775653590882, 'date': 'Sun, 5 Jul 2020 12:00:01 GMT', 'inverseRate': 27.951970114527}
```

## 6. Last But Not Least

### Description

At this stage, you need to specify what currency you want to exchange. Imagine that you came to the bank with some money in your pocket. You want to choose the best currency to exchange your money for. First, read the currency to exchange, then read the currency you might exchange your money for and the amount of money you want to exchange. Notice that the input number can have a fractional part!
```
There is a different amount of currencies in different tests. Checking if input is empty might be really useful.
```
Parse the data from FloatRates. You can store it in any collection you want. It's called caching – a simple way to speed up the program. If we need to exchange the same currencies that we have already changed, we won't need to connect to the Internet, we only need to refer to the data in our cache.
```
The very first currency is the one you want to exchange.
```
Check the cache — the required currency might be already in there, print the result afterward. Output the amount of money that the bank employee should give you. 

### Objective

You're in the bank. Think about how much and what kind of currency you have.

1. Take the currency code, the amount of money the user has, and the currency code that the user wants to receive as the user input.
2. Retrieve the data from FloatRates as in the previous exercises.
3. Save the exchange rates for USD and EUR.
4. Read the currency to exchange for and the amount of money.
5. Take a look at the cache. Maybe you already have what you need?
6. If you have the currency in your cache, calculate the amount.
7. If not, get it from the site, and calculate the amount.
8. Save all the information to your cache.
9. Print the results.
10. Repeat steps 4-9 until there is no currency left to process.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Be aware that the dictionary elements are unordered.

Example 1:
```
> ILS
> USD
> 45
Checking the cache...
Oh! It is in the cache!
You received 13.84 USD.
> RSD
> 57
Checking the cache...
Sorry, but it is not in the cache!
You received 1684.41 RSD.
> EUR
> 33
Checking the cache...
Oh! It is in the cache!
You received 8.38 EUR.
```
Example 2:
```
> USD
> EUR
> 20
Checking the cache...
Oh! It is in the cache!
You received 16.52 EUR.
> NOK
> 45
Checking the cache...
Sorry, but it is not in the cache!
You received 382.1 NOK.
> SEK
> 75
Checking the cache...
Sorry, but it is not in the cache!
You received 624.66 SEK.
> NOK
> 55
Checking the cache...
Oh! It is in the cache!
You received 467.02 NOK.
> ISK
> 91
Checking the cache...
Sorry, but it is not in the cache!
You received 11708.38 ISK.
```
