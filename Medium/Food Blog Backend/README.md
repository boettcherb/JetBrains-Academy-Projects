# Food Blog Backend

### About this project
You will create a function that takes a website address and a number of webpages as input arguments and then goes all over the website saving every news article on the page to a separate .txt file on your computer.

### Learning Outcomes
After finishing the project, you’ll know how to send HTTP-requests and process the responses, how to work with an external library, library documentation, and how to use it for parsing the website data. You will also find out how to make your program save results to a file with the help of Python.

### Run

Requirements:
- Python 3.9
`python foodblogbackend.py`

# Code it yourself:

## 1. Create Dictionaries

### Description

Your great-grandmother asked you to copy "to these computers" all the recipes that she had been collecting in her notebook for several decades. You think that this task can be a good opportunity to practice your skills and build a tool that would collect the data in a database. It will allow you to create a database of recipes that you will be able to use in the blog with the great-grandma's recipes. You started by writing down the names of the ingredients and measures that Grandma used. It also may be good to assign different dishes to different times of the day. It's time to create a database and dictionaries!

### Theory

SQLite3 is a relational database management system. You can use it for free; it is licensed as Public Domain. The system implements most of the SQL standards. For this project, we will use the basic SQLite3 functions.

First, import the sqlite3 library:
```
import sqlite3
```
To connect your script to an SQLite database, use the connect() method from the sqlite3 library and create a database cursor with the cursor() method:
```
conn = sqlite3.connect(data_base_name)
cursor_name = conn.cursor()
```
To execute an SQL query, use the execute() cursor method. This method will return an object that contains the result of the query. For example:
```
result = cursor_name.execute(SQL_query_as_string)
```
Another two important methods are close() and commit(). Remember that you need to confirm the SQL queries with the commit command. Otherwise, the data will be lost. At the end of your code, disconnect your database. Both methods are related to the database connection:
```
conn.commit()
conn.close()
```
If you need more information, the SQLite Tutorial will help you!

### Objectives

1. Create a database. Pass the name of the database to the script as an argument.
2. Create a table named meals with two columns: meal_id of an integer type with the primary key attribute, and meal_name of a text type and with the unique and not null attribute.
3. Create a table named ingredients with two columns: ingredient_id of an integer type with the primary key attribute and ingredient_name of a text type with the unique and not null attribute. Multi-word ingredients are out of scope, you don't need to implement their support in your script.
4. Create a table named measures with two columns: measure_id of an integer type with the primary key attribute, and measure_name of a text type with the unique attribute.
5. Populate the tables. Those tables are the dictionaries for the Food Blog system, you need to fill them once for the rest of the stages.
```
    data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
            "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
            "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}
```
6. Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.
7. Do not add other items to the dictionaries. This may affect the test results in this and the next stages.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
> python food_blog.py food_blog.db
```

## 2. Time for Recipies!

### Description

It is time to create the main recipe table. You decided to store the recipe name and description in the main table. You wanted to indicate which meal suits the dish best, but your great-grandmother told you that it doesn't have to be just one meal. So you have to think about the solution. You also need to build a tool that will allow you to fill your database with data.

### Objectives

1. Create a table named `recipes` with three columns: `recipe_id` of an integer type with the primary key attribute, `recipe_name` of a text type with the not-null attribute, and `recipe_description` of a text type.
2. Prepare a simple system that allows you to populate this table. Ask for the recipe name and the cooking directions, and insert the data into the table.
3. When a zero-length string is entered for the recipe name the script should terminate. Remember to commit your changes and close the database.
4. Remember! You can print anything you want. Tests will check only the database file that your script will create and populate.
5. You do not need to validate the entered data. The tests will pass the correct values.

### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
```
> python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: > Cold milk
Recipe description: > Freeze milk
Recipe name: > Hot milk
Recipe description: > Boil milk
Recipe name: >
```
