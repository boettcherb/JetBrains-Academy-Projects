# Markdown Editor

### About this project
Markdown is a special plain text formatting language that is extremely popular among developers. It is used in documents, research articles, Github README files, and other things. In this project, you will write an editor that will be able to recognize several tags, structures, and save your results to a file.

### Learning Outcomes
Practice list operations, file handling, functions, scopes, and a lot of other things. Make a handy and useful tool that uses the markdown language!

### Run

Requirements:
- Python 3.9
`python markdowneditor.py`

# Code it yourself:

## 1. Meet the Markdown

### Description

Welcome to the first stage of the project!

If you have worked with the markdown, you will probably recognize the following syntax:
```
# The Beatles
One may say that they were the most famous **rock band** ever.
The legendary **line-up** comprised the following people:
* *John Lennon*
* *Paul McCartney*
* *George Harrison*
* *Ringo Starr*
```
Yes! It is a raw markdown code. It translates into:

# The Beatles
One may say that they were the most famous **rock band** ever.
The legendary **line-up** comprised the following people:
* *John Lennon*
* *Paul McCartney*
* *George Harrison*
* *Ringo Starr*

### Objectives

Determine and print the source (raw) markdown code of the markdown snippet below. Show your understanding of the syntax basics. You can use the Markdown Guide as it covers all the necessary topics.

Below is the snippet to complete this stage. Once you write it in the markdown syntax, put it into triple quotes and print it:

# John Lennon

or ***John Winston Ono Lennon**** was one of *The Beatles*.
Here are the songs he wrote I like the most:

* Imagine
* Norwegian Wood
* Come Together
* In My Life
* ~~Hey Jude~~ (that was *McCartney*)

### Example

Take a look at the snippet below:

# The List of Albums
During their history, a lot of great albums were released.
These are my favorite:
1. Abbey Road
2. Rubber Soul
3. Revolver
4. A Hard Day's Night

To complete this stage, you would have needed to print the following:

```
# The List of Albums
During their history, a lot of great albums were released.
These are my favorite:
1. Abbey Road
2. Rubber Soul
3. Revolver
4. A Hard Day's Night
```

## 2. How do I use it?

### Description

Before we start implementing the project, we need to think about the functionality. Remember the Markdown Guide from the previous stage? Let's go through it one more time and recall the basic features:

- plain — a normal text without any formatting
- **bold**/*italic* — self-explanatory
- inline-code — for example, `python editor.py`
- link — for example, [google.com](https://google.com)
- header — look at the header of this stage.
- unordered-list — this very list is an example of an unordered list
- ordered-list — a list with enumerated elements
- new-line — switches to the next line

In this stage, you need to implement these features in your editor. Let's also add special commands to our tool:

- `!help` — prints available syntax commands.
- `!done` — saves the markdown and exits the app.

Let's do it!

### Objectives

Implement the help function that will print available syntax commands, which we have indicated above, as well as the special commands. When called, it should print the following:
```
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
```
Implement the exit function that exits the editor without saving.

Ask a user for input:
```
Choose a formatter:
```
`!help` prints the help page, `!done` exits the editor.

If the input contains one of the correct formatters (plain, bold, italic, etc.), ask for the input once again.

If the input contains no formatters or unknown command is sent, print the following message and ask for input again: `Unknown formatting type or command`

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Example 1:

```
Choose a formatter: > non-existing-formatter
Unknown formatting type or command
Choose a formatter: > !help
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done
Choose a formatter: > header
Choose a formatter: > ordered-list
Choose a formatter: > !done
```

## 3. Text Formatting

### Description

Congratulations! You've made it to the most interesting part of the project. Now we will try to implement the formatters that we have discussed before. For your convenience, I will copypaste them from the previous stage:

- plain
- **bold**/*italic*
- `inline-code`
- link
- header
- new-line

We do not include ordered and unordered lists, for now. This also means that you should delete them from the list shown when a user asks for the `!help` function. But we will get to them in the next stage!

### Objectives

Implement a separate function for each of the formatters. It will keep your code structured. With functions, you also will be able to find and fix a bug with ease if something is wrong.

The program should work in the following way:

1. Ask a user to input a formatter.
2. If the formatter doesn't exist, print the following error message: `Unknown formatting type or command`
3. Ask a user to input a text that will be applied to the formatter: `Text: <user's input>`.
4. Save the text with the chosen formatter applied to it and print the markdown. Each time you should print out the whole text in markdown accumulated so far.

Different formatters may require different inputs.

The new-line formatter does not require text input.

Plain, bold, italic, and inline-code formatters require only text input, and should not add an extra space or line break at the end:
```
Text: > Some text
```
Headers require a level and text. A level is a number from 1 to 6. Don't forget to check it too: if it is out of bounds, print the corresponding error: `The level should be within the range of 1 to 6`. Also, remember that a heading automatically adds a new line in the end.
```
Level: > 4
Text: > Hello World!
```
Link requires a label and a URL:
```
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
```

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Example 1: the header formatter automatically adds a line break
```
Choose a formatter: > non-existing-formatter
Unknown formatter type or command
Choose a formatter: > header
Level: > 4
Text: > Hello World!
#### Hello World!

Choose a formatter: > plain
Text: > Some plain text
#### Hello World!
Some plain text
Choose a formatter: > new-line
#### Hello World!
Some plain text

Choose a formatter: > link
Label: > Tutorial
URL: > https://www.markdownguide.org/basic-syntax/
#### Hello World!
Some plain text
[Tutorial](https://www.markdownguide.org/basic-syntax/)
Choose a formatter: > !done
```

## 4. Ordered and Unordered Lists

### Description

There is one more feature that can be very useful! Imagine going to a grocery store, I bet you would need some kind of a list there. Markdown lists are straightforward; there are two kinds of them: ordered and unordered. I think you've already guessed that the difference between them is that an ordered list itemizes the elements (1., 2., 3., and so on) while an unordered list doesn't do it.

Remember the ordered-list and unordered-list formatters we skipped in the last stage? Let's get back to them!

### Objectives

Implement the ordered-list and unordered-list formatters. You may want to separate the implementation into two different functions, but I suggest keeping them in one; try to get an idea of how to do it!

Both of the formatters require the following input:
```
Number of rows: > 3
Row #1: > First element
Row #2: > Second element
Row #3: > Third element
```
Don't forget to check that the number of rows is greater than zero! Otherwise, print the following message: `The number of rows should be greater than zero`

Don't forget about the formatters that we have implemented in the previous stages.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Example 1: the formatters automatically add a line break
```
python markdown-editor.py
Choose a formatter: > ordered-list
Number of rows: > 3
Row #1: > First element
Row #2: > Second element
Row #3: > Third element
1. First element
2. Second element
3. Third element

Choose a formatter: > unordered-list
Number of rows: > 2
Row #1: > Fourth element
Row #2: > Fifth element
1. First element
2. Second element
3. Third element
* Fourth element
* Fifth element

Choose a formatter: > unordered-list
Number of rows: > -2
The number of rows should be greater than zero
Number of rows: > 2
Row #1: > Sixth element
Row #2: > Seventh element
1. First element
2. Second element
3. Third element
* Fourth element
* Fifth element
* Sixth element
* Seventh element

Choose a formatter: > !done
```

## 5. Save the Results

### Description

By this moment, our program can recognize some of the formatters and special commands, it can also print the results and exit. We need to implement yet another very useful feature — the ability to save the text to a file.

### Objectives

Modify your `done` function that was implemented in the second stage. Apart from exiting the program, it should save the final result of a session to a file, let's call it *output.md*. Create this file in the program directory. If it already exists, overwrite this file. The file should include the result of the last session.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Example 1:
```
Choose a formatter: > header
Level: > 1
Text: > Hello World!
# Hello World!

Choose a formatter: > plain
Text: > Lorem ipsum dolor sit amet, consectetur adipiscing elit
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit
Choose a formatter: > line-break
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit

Choose a formatter: > ordered-list
Number of rows: > 3
Row #1: > dolor
Row #2: > sit
Row #3: > amet
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit
1. dolor
2. sit
3. amet

Choose a formatter: > !done
```
