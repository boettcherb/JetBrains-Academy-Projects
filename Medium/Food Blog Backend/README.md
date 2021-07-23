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

## 3. Many-to-many Relations

### Description

On this stage, you need to create many-to-many relations between two tables. One dish can be served at different mealtimes, and one meal can consist of different dishes. However, this model is not recommended. Instead, we suggest you implementing a cross-reference table that contains primary key attributes from the two tables in relation. 

### Theory

In SQLite, you can use two methods to retrieve entries from the returned object: `fetchall()` and `fetchone()`. The first method returns all matching entries as a list of tuples, while the second method returns the next data row or `None` if there are no more rows:
```
result = cursor_name.execute(SQL_query_as_string)
all_rows = result.fetchall()  # all_rows stores a list of tuples

result = cursor_name.execute(SQL_query_as_string)
next_row = result.fetchone()  # returns a single tuple
```
A useful attribute of the cursor object is `lastrowid`. When the **INTEGER PRIMARY KEY** column is auto-incremented, this attribute stores the value of this key. It allows you to know the `PRIMARY KEY` attribute of the entry. Don't forget to commit your changes!
```
result = cursor_name.execute(SQL_INSERT_query_as_string).lastrowid
```
To use foreign keys in your SQLite database, you need to turn them on first by executing the command:
```
PRAGMA foreign_keys = ON;
```
When creating a table, you need to associate the foreign key with the given column:
```
CREATE TABLE IF NOT EXISTS table1(table1_id INTEGER PRIMARY KEY, table2_id INTEGER NOT NULL,
FOREIGN KEY(table2_id) REFERENCES table2(table2_id));
```
Once you indicated the `FOREIGN KEY` parameter in your code, the entries associated with this parameter cannot be deleted as long as this parameter persists. In the example above, we won't be able to remove the entries from the `table2` until we remove the linking entry from the `table1`.

You can refer to the Foreign Key section of the SQLite tutorial for more details.

### Objectives

1. Create a table named `serve` with three columns: `serve_id` of an `INTEGER` type with the `PRIMARY KEY` attribute, and `recipe_id` and `meal_id`, both of `INTEGER` type with the `NOT NULL` attribute.
2. Assign the `recipe_id` and `meal_id` as Foreign Keys to the following tables: `recipes` (the `recipe_id` column) and `meals` (the `meal_id` column).
3. Once a user has entered a dish name and a recipe description print all available meals with their primary key numbers.
4. Ask a user when this dish can be served. Users should input numbers separated by a space.
5. Input values to the `serve` table. If the user has selected three meals when the dish can be served, there should be three new entries in the `serve` table.
6. You do not need to validate the entered data. The tests will enter the correct values.
7. Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.
```
> python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: > Hot milk
Recipe description: > Boil milk
1) breakfast  2) brunch  3) lunch  4) supper 
When the dish can be served: > 1 3 4
Recipe name:
```

## 4. Too Many Ingredients

### Description

It's time to add ingredient quantities, measures, and ingredient names to your recipes! You noticed that some ingredients have long names and measures rarely start with the same letter. You decided to build your backend so that you do not have to enter full names when completing the database. You will encounter a many-to-many relationship again, this time between three tables, so you decided to introduce an intermediate table that would link all three tables. 

### Objectives

1. Create a table named `quantity` with five columns: `quantity_id` of an `INTEGER` type with the `PRIMARY KEY` attribute, and four other columns: `measure_id`, `ingredient_id`, `quantity` and `recipe_id`. They should be of an `INTEGER` type with the `NOT NULL` attribute.
2. Assign the following columns `measure_id`, `ingredient_id` and `recipe_id` as Foreign Keys to the following tables (`columns`): measures (`measure_id`), ingredients (`ingredient_id`), and recipes (`recipe_id`)
3. After asking a user about certain mealtime, make a loop that will gather information about the ingredients. The ingredients should be entered in the following format: `quantity measure ingredient`.
4. Pressing `<Enter>` should finish the information gathering.
5. The measure parameter should start with a string provided by a user. If there is more than one measure that starts with the provided string, ask the user again. For example `tbs` and `tbsp` both start with the `t`. So the `1 t sugar` entry should not pass.
6. Mind that the `measures` table contains an entry where the `measure_name` is empty string, it means, that the measure could be not provided. In this case, use this entry to relate tables. For example, `1 strawberry` should have a `measure_key` from the entry with an empty name.
7. The ingredient parameter should contain strings provided by a user. If there is more than one ingredient that contains the provided string, ask the user again. For example `strawberry` and `blueberry` both contain `berry` as part of the string. So the `10 kg berry` entry should not pass.
8. Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.

### Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Example 1:
```
> python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: Hot milk
Recipe description: Boil milk
1) breakfast  2) brunch  3) lunch  4) supper 
Enter proposed meals separated by a space: 1 3 4
Input quantity of ingredient <press enter to stop>: 10 ml milk
Input quantity of ingredient <press enter to stop>: 
Recipe name:
```
Example 2:
```
> python food_blog.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: Hot milk
Recipe description: Boil milk
1) breakfast  2) brunch  3) lunch  4) supper 
Enter proposed meals separated by a space: 1 3 4
Input quantity of ingredient <press enter to stop>: 250 ml m
Input quantity of ingredient <press enter to stop>: 1 t sugar
The measure is not conclusive!
Input quantity of ingredient <press enter to stop>: 1 tbs sugar
Input quantity of ingredient <press enter to stop>: 1 berry
The ingredient is not conclusive!
Input quantity of ingredient <press enter to stop>: 1 blueberry
Input quantity of ingredient <press enter to stop>: 
Recipe name:
```
