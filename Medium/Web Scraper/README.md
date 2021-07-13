# Web Scraper

### About this project
You will create a function that takes a website address and a number of webpages as input arguments and then goes all over the website saving every news article on the page to a separate .txt file on your computer.

### Learning Outcomes
After finishing the project, you’ll know how to send HTTP-requests and process the responses, how to work with an external library, library documentation, and how to use it for parsing the website data. You will also find out how to make your program save results to a file with the help of Python.

### Run

Requirements:
- Python 3.9
`python webscraper.py`

# Code it yourself:

## 1. Wanna talk to the Internet?

### Description

We use the Internet everyday. Have you ever wondered how your computer communicates with the Global Web? In this stage, we'll learn how to talk to the Internet from your Python script — and interpret the replies! Your program should send an HTTP request to a URL received from the user input. The user input can be a Quotable resource `http://api.quotable.io/quotes/-CzNrWMGIg8V`. In this case, the program should print out the Quote extracted from the `json` body response.

The user input may also contain an invalid URL or a non-existing quote resource, for example, `http://api.quotable.io/quotes/1`, or a different Quotable page (`http://api.quotable.io/authors`). Use `if-else` statements to check the `status_code` or the `json` body response to print out the `Invalid quote resource!` error message when the response code is different from 200, or when there is no quote in the `json` body response. Your program should ask for input. 

### Objectives

In this stage, your program should:

1. Send an HTTP request to a URL received from the user input.
2. Print out the Quote content extracted from the json body response.
3. Print out the Invalid quote resource! error message if there's no quote or something goes wrong.

### Examples

The greater-than symbol followed by space (`> `) represents the user input. Note that it's not part of the input.

Example 1
```
Input the URL:
> http://api.quotable.io/quotes/-4WQ_JwFWI

The three great essentials to achieve anything worth while are: Hard work, Stick-to-itiveness, and Common sense.
```
Example 2
```
Input the URL:
> http://api.quotable.io/quotes/asdfgh

Invalid quote resource!
```
