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
