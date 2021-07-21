import sys
import sqlite3


def main():
    con = sqlite3.connect(sys.argv[1])
    cur = con.cursor()
    cur.execute("CREATE TABLE meals ("
                "    meal_id INT PRIMARY KEY,"
                "    meal_name VARCHAR(20) UNIQUE NOT NULL"
                ");")
    cur.execute("CREATE TABLE ingredients ("
                "    ingredient_id INT PRIMARY KEY,"
                "    ingredient_name VARCHAR(20) UNIQUE NOT NULL"
                ");")
    cur.execute("CREATE TABLE measures ("
                "    measure_id INT PRIMARY KEY,"
                "    measure_name VARCHAR(20) UNIQUE"
                ");")
    cur.execute("INSERT INTO meals VALUES (0, 'breakfast'), (1, 'brunch'), "
                "(2, 'lunch'), (3, 'supper');")
    cur.execute("INSERT INTO ingredients VALUES (0, 'milk'), (1, 'cacao'), "
                "(2, 'strawberry'), (3, 'blueberry'), (4, 'blackberry'), "
                "(5, 'sugar');")
    cur.execute("INSERT INTO measures VALUES (0, 'ml'), (1, 'g'), (2, 'l'), "
                "(3, 'cup'), (4, 'tbsp'), (5, 'tsp'), (6, 'dsp'), (7, '');")
    con.commit()
    cur.execute("CREATE TABLE recipes ("
                "    recipe_id INT PRIMARY KEY,"
                "    recipe_name VARCHAR(20) NOT NULL,"
                "    recipe_description VARCHAR(100)"
                ");")
    recipe_name = input("Recipe name: ")
    recipe_id = 0
    while recipe_name != "":
        recipe_description = input("Recipe description: ")
        cur.execute(f"INSERT INTO recipes VALUES ({recipe_id},"
                    f"'{recipe_name}', '{recipe_description}');")
        recipe_id += 1
        recipe_name = input("Recipe name: ")
    con.commit()
    con.close()


if __name__ == "__main__":
    main()
