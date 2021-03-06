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

## 4. The Soup is Real

### Description

We now have a good deal of knowledge and experience, so let's put it all together and create your first real web scraper. Most of the time, the reason why people create parse-and-scrape programs is to automate the routine tasks of retrieving large data from a website. For example, every machine learning task requires some **train data**. Let's imagine you're doing research based on the recent science news. For that research, you'll need to have the most recent articles with the type "News" that are posted on the Nature journal website. Each article should be saved to a separate *.txt* file named after the article's title.

### Objectives

1. Create a program that takes the `https://www.nature.com/nature/articles` URL and then goes over the page source code searching for articles.
2. Detect the article type and the link to view the article tags and their attributes.
3. Save the contents of each article of the type "News" to a separate file named *%article_title%.txt*. Replace the whitespaces with underscores and remove punctuation marks in the filename (`str.maketrans` and `string.punctuation` will be useful for this). Also, strip all trailing whitespaces in the article body and title.
4. (Optional) You may output some result message once the saving is done, but it is not required.

We need to inspect each article to find the tags that represent the article's contents. If you take a closer look at the source code, you will see that every article is enclosed in a pair of `<article>` tags. Then, each article type is hidden inside a `<span>` tag containing the `data-test` attribute with the `article.type` value. Also, every article includes a link to the article's contents, which is placed inside the `<a>` tag with the `data-track-action="view article"` attribute. Once the article page is loaded, save its body wrapped in the `<div>` tag (look for "body" in the `class` attribute).
```
Make sure your output file is binary with the UTF-8 character encoding. 
```

### Example

This time, the program should not take the URL from the input: hard-code it inside the program. Below is an example of the output:
```
Saved articles:  ['COVID_research_updates_Immune_responses_to_coronavirus_persist_beyond_6_months.txt', 'What_scientists_really_think_about_the_ethics_of_facial_recognition_research.txt', 'Legendary_Arecibo_telescope_will_close_forever_scientists_are_reeling.txt', 'What_the_data_say_about_asymptomatic_COVID_infections.txt']
```
The main goal is to save the articles with the correct article bodies once the program has been executed.

## 5. Soup, Sweet Soup

### Description

You've done an amazing job in the previous stage! Remember we mentioned retrieving large data? Let's improve your program by making it parse multiple website pages. To make it even more useful, let's also implement the opportunity to parse several kinds of articles at once. 

### Objectives

1. Improve your code so that the function can take two parameters from the user input: the number of pages (an integer) and the type of articles (a string). The integer with the number of pages specifies the number of pages on which the program should look for the articles.
2. Go back to the `https://www.nature.com/nature/articles` website and find out how to navigate between the pages with the `requests` module changing the URL.
3. Create a directory named `Page_N` (where N is the page number) for each page in the desired category, and put all the articles that are found on the page with the matched type to this directory.
4. Save the articles to separate `*.txt` files. Keep the same processing of the titles for the filenames as in the previous stage. You can give users some feedback on completion, but it is not required.

If there's no articles on the page, your program should still create a folder, but in this case the folder would be empty.

### Example

The program takes two input values from the user and then continues to process the Nature website data.

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
> 4
> Nature Briefing
Saved all articles.
```
The main goal is to save the articles with the correct article bodies once the program has been executed.
