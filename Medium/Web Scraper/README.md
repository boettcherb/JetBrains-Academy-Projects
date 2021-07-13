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

## 2. The Beautiful Soup Ingredients

### Theory

Some Internet pages might get automatically translated according to your computer's settings. Although this might be useful in everyday life, in this project we ask you to output the data in English. To force `requests` library to return a page in English, you can use `headers` with `Accept-Language` parameter set to the value `en-US,en;q=0.5`:
```
response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
```
Note that the structure of the page might be different in cases when you use this header and when you don't (even if your default language is English). 

### Description

We know how to send HTTP requests and get responses. In the previous stage, the example URL responded with the `json` body, this is how the `REST` resources communicate with a client. We, humans, go to websites to access the Internet. We also have browsers, but sometimes we need to parse the website's content automatically. Parsing is one of the ways to scrape a webpage.

Parsing website data begins with the inspection of the page source code with browser built-in tools. Usually, the desired information can be distinguished by some unique attributes or a set of attributes, for example, a `css class` name. We need to determine these attributes and then make our parsing tool (in our case, the **beautifulsoup** library) do the magic for us. 

### Objectives

1. Feed your program a link to a movie description. This is an example of a correct link: `https://www.imdb.com/title/tt0080684/`.
2. Inspect the page and find out how the movie's title and description are stored in the source code.
3. Download the webpage content, parse it using the beautifulsoup library, and print out the movie's original title and description in a dictionary.

If the received page doesn't have a movie description or is not an IMDb resource, the program should respond with the `Invalid movie page!` message, just like in the previous stage.

### Examples

A user inputs a URL with a movie description to store it in the response dictionary. If the link is not correct or does not contain a movie original title and description, the program responds with an error message.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input. Each example corresponds to a separate execution.

Example 1
```
Input the URL:
> https://www.imdb.com/title/tt0080684/

{"title": "Star Wars: Episode V - The Empire Strikes Back", "description": "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader and a bounty hunter named Boba Fett all over the galaxy."}
```
Example 2
```
Input the URL:
> https://www.imdb.com/name/nm0001191/

Invalid movie page!
```
Example 3
```
Input the URL:
> https://www.google.com/

Invalid movie page!
```

## 3. What the File?

### Theory

Apart from writing files in the usual text mode, it is also possible to write files in binary mode. It means that Python won't encode the data while writing it to the file. This can be done by passing the argument `"wb"` to the `open()` function instead of the usual `"w"`:
```
file = open('file.html', 'wb')
```
To retrieve a page's content while using `requests` library, `content` attribute can be used:
```
page_content = requests.get(inp_url).content
```
Please, use these bits of knowledge in your code for this stage.

### Description

In previous stages, we retrieved the results and printed them out on the screen. It's handy for one-time running programs or for debugging, but if we want to reuse the data (and that's the case most of the time), storing it is more effective. The simplest way to store data is to write it to a file on your computer.

In this stage, we are going to store the state of a webpage at the moment when the program is executed. It means that we need to get its source code, the content, and save it to a *.html* file. 

### Objectives

1. Create a program that retrieves the page's source code from a user input URL. Please, don't decode the page's content.
2. Save the page's content to the source.html file. Please, write the file in binary mode.
3. Print the Content saved. message if everything is OK (Don't forget to add a check for the status_code).
4. If something is wrong, print the message The URL returned X, where X is the received error code.

### Examples

The program receives a URL to retrieve the data from the user input, saves the data to the source.html file, and responds with the successful completion message. Otherwise, it should notify a user about an error.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input. Each example corresponds to a separate execution.

Example 1
```
Input the URL:
> https://www.facebook.com/

Content saved.
```
Example 2
```
Input the URL:
> http://google.com/asdfg

The URL returned 404!
```
