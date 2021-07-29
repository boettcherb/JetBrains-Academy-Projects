# To-Do List

### About this project
To-Do list can improve your work and personal life. You can use it to reduce the stress in your life and get more done in less time. It also helps you become more reliable for other people and save time for the best things in life. So let's implement it!

### Learning Outcomes
To-Do list that will help you manage your tasks. You will practice using loops, conditions and statement branches. And also you will learn the basics of SQLAlchemy to manage SQLite database on python!

### Run

Requirements:
- Python 3.9
`python todolist.py`

# Code it yourself:

## 1. Plan It

### Description

Do you have 10 minutes a day to add $4000 to your monthly income?

This is the average income difference between people who write down their goals and those who don’t. That’s one of many reasons why having a To-Do list can improve your work and personal life. You can use it to reduce the stress in your life and get more done in less time. It also helps you become more reliable for other people and save time for the best things in life.

In this project, you will create a To-Do list that will help you organize your life.

### Objectives

To begin with, develop a simple list of 4 tasks. Your program must print exactly the same list as given in the example.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Output:
```
Today:
1) Do yoga
2) Make breakfast
3) Learn basics of SQL
4) Learn what is ORM
```

## 2. I am an Alchemist!

### Description

It's very upsetting when the data about your to-do tasks disappear after the program is completed. To avoid this problem, you need to create a database where you can store all the necessary information about your tasks. We will use SQLite to create the database and SQLAlchemy to manage the database from Python.

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper (ORM) that gives developers the full power and flexibility of SQL.

First, you need to create your database file. To create it, you should use the `create_engine()` method, where `file_name` is the database file name:
```
from sqlalchemy import create_engine

engine = create_engine('sqlite:///file_name?check_same_thread=False')
```
`check_same_thread=False` argument allows connecting to the database from another thread. It's required for the test purpose, otherwise, you will get an exception.

Once you've created your database file, you need to create a table in it. First, create a model class that describes the table in the database. All model classes should inherit from the `DeclarativeMeta` class that is returned by `declarative_base()`:
```
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

Base = declarative_base()


class Table(Base):
    __tablename__ = 'table_name'
    id = Column(Integer, primary_key=True)
    string_field = Column(String, default='default_value')
    date_field = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field
```
All information about the table is described in its model class.

- `Table` is the name of the model class. It is used to access data from the table it describes. The name of the class can be anything.
- `__tablename__` specifies the table name in the database.
- `id` is an integer column of the table; `primary_key=True` says that this column is the primary key.
- `string_field` is a string column; `default='default_value'` says that the default value of this column is `'default_value'`.
- `date_field` is a column that stores the date. SQLAlchemy automatically converts the SQL `date` into a Python `datetime` object.
- `__repr__` method returns a string representation of the class object. In the ORM concept, each row in the table is an object of a class.

After we've described our table, it's time to create it in our database. All we need is to call the `create_all()` method and pass `engine` to it:
```
Base.metadata.create_all(engine)
```
This method creates a table in our database by generating SQL queries according to the models we described.

Now we can access the database and store data in it. To access the database, we need to create a session:
```
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
```
The `session` object is the only thing you need to manage the database. To create a row in our table, you need to create an object of the model class and pass it to the `add()` method:
```
new_row = Table(string_field='This is a string field!',
         date_field=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
session.add(new_row)
session.commit()
```
To get all rows from the table, you can pass the model class to the `query()` method that selects all rows from the table represented by a model class:
```
rows = session.query(Table).all()
```
The `all()` method returns all rows from the table as a Python list. Each element of this list is an object of the model class. You can access the row fields by their names:
```
first_row = rows[0] # In case rows list is not empty

print(first_row.string_field) # Will print the value of the string_field
print(first_row.id) # Will print the id of the row
print(first_row) # Will print the string that was returned by the __repr__ method
```

### Objectives

Let's store the data about our tasks in the database. Here's what you need to do:

- Create a database file. Its name should be `todo.db`.
- Create a table in this database. The table name should be `task`.

The table `task` should have the following columns:

- Integer column named `id`. It should be the `primary key`.
- String column named `task`.
- Date column named `deadline`. It should have the date when the task was created by default. You can use `datetime.today()` method.

Also, you need to implement a menu that will make your program more convenient. The menu should have the following items:

- Today's tasks. Prints all tasks for today.
- Add task. Asks for task description and saves it in the database.
- Exit.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Output:
```
1) Today's tasks
2) Add task
0) Exit
> 1

Today:
Nothing to do!

1) Today's tasks
2) Add task
0) Exit
> 2

Enter task
>Prepare presentation
The task has been added!

1) Today's tasks
2) Add task
0) Exit
> 1

Today:
1. Prepare presentation

1) Today's tasks
2) Add task
0) Exit
> 0

Bye!
```

## 3. Deadlines are Scary

### Description

Everyday, we’re surrounded by thousands of small distractions, facts, and bits of odd information. When you’re on a deadline, you don’t have time for all this fluff. You need to focus on the task at hand, so you can’t afford to spend hours on Pinterest, chatting at the water cooler with your coworkers, or watching re-runs on TV. At this point in time, the deadline takes precedence.

So let's add the ability to set deadlines for our tasks. Python `datetime` module will help us work with dates.

Here are some methods that might help you:
```
from datetime import datetime, timedelta

datetime.today() # return current date and time.
datetime.today().date() # current date without time
datetime.today().time() # current time without date

datetime.strptime(date_string, format) # return a datetime corresponding to date_string, parsed according to format.
# Format example: '%Y-%m-%d' - '2020-04-24'

today = datetime.today()
today.day # the day of a current month.
today.strftime('%b') # the short name of the current month. I.e 'Apr'
today.weekday() # return the day of the week as an integer, where Monday is 0 and Sunday is 6.

yesterday = today - timedelta(days=1) # a timedelta object represents a duration, the difference between two dates or times.
day_after_tomorrow = today + timedelta(days=2)
```
To select rows from the table with some condition, you can use `filter()` method that accepts the condition by which to select rows:
```
from datetime import datetime

today = datetime.today()
rows = session.query(Table).filter(Table.date == today.date()).all()
```
In the code snippet above, we selected all rows from `Table` where the date column equals today's date.

To sort selected data, you can use `order_by()` that accepts a column by which you need to sort data:
```
# select all rows ordered by the date column
session.query(Table).order_by(Table.date).all()

# select all rows where string_fields starts with 'L'. The result is ordered by date column
session.query(Table).filter(Table.string_field.startswith('L'))).order_by(Table.date).all()
```

### Objectives

Add the following items to your menu:

- **Week's tasks**: prints all tasks for 7 days from today.
- **All tasks**: prints all tasks sorted by deadline.

Now **Add task** item should ask for the deadline of the task. Users should input the deadline in this format: **YYYY-MM-DD**.

Also, **Today's tasks** item should print today's date.

See the format of the output in the example.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Output:
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
> 1

Today 26 Apr:
Nothing to do!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
> 4

Enter task
>Meet my friends
Enter deadline
>2020-04-28
The task has been added!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
> 2

Sunday 26 Apr:
Nothing to do!

Monday 27 Apr:
Nothing to do!

Tuesday 28 Apr:
1. Meet my friends

Wednesday 29 Apr:
Nothing to do!

Thursday 30 Apr:
1. Math homework
2. Call my mom

Friday 1 May:
1. Order a new keyboard 

Saturday 2 May:
Nothing to do!
>3

All tasks:
1. Meet my friends. 28 Apr
2. Math homework. 30 Apr
3. Call my mom. 30 Apr
4. Order a new keyboard. 1 May

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
> 0

Bye!
```

## 4. Bye, Completed Tasks

### Description

Planning is one thing, but when we need to knuckle down and put our plans into action, we tend to push our tasks back further and further until the last minute, or worse — past the established deadline. It happens to the best of us!

In this stage, let's implement the ability to see missed tasks and delete them.

To delete a row from a table, you need to use the `delete()` method that accepts an object to delete. As you remember, each row is represented by a Python object:
```
from datetime import datetime

# delete all rows where date column equals today's date
session.query(Table).filter(Table.date == datetime.today().date()).delete()

# delete a specific row
rows = session.query(Table).filter(Table.date < datetime.today().date()).all()
specific_row = rows[0] # in case rows is not empty
session.delete(specific_row)

# don't forget to commit changes
session.commit()
```

### Objectives

Add the following items into your menu:

- **Missed tasks**: prints all tasks whose deadline was missed, that is, tasks whose deadline date is earlier than today's date.
- **Delete task**: deletes the chosen task. Print 'Nothing to delete' if the tasks list is empty.

**Missed tasks** should print the tasks ordered by the deadline date.

**Delete task** should print all the tasks sorted by the deadline date and ask to enter the number of the task to delete.

See in the example what your program should look like.

### Example

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

Output:
```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 4

Missed tasks:
1. Learn the for-loop. 19 Apr

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 6

Choose the number of the task you want to delete:
1. Learn the for-loop. 19 Apr
2. Learn the basics of SQL. 29 Apr
> 1
The task has been deleted!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 4

Missed tasks:
Nothing is missed!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
> 0

Bye!
```
