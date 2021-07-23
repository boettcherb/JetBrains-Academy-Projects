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
    cur.execute("CREATE TABLE serve ("
                "    serve_id INT PRIMARY KEY,"
                "    recipe_id INT NOT NULL,"
                "    meal_id INT NOT NULL,"
                "    CONSTRAINT fk_recipes FOREIGN KEY (recipe_id)"
                "    REFERENCES recipes(recipe_id),"
                "    CONSTRAINT fk_meals FOREIGN KEY (meal_id)"
                "    REFERENCES meals(meal_id)"
                ");")
    cur.execute("CREATE TABLE quantity ("
                "    quantity_id INT PRIMARY KEY,"
                "    measure_id INT NOT NULL,"
                "    ingredient_id INT NOT NULL,"
                "    quantity INT NOT NULL,"
                "    recipe_id INT NOT NULL,"
                "    CONSTRAINT fk_measures FOREIGN KEY (measure_id)"
                "    REFERENCES measures(measure_id),"
                "    CONSTRAINT fk_ingredients FOREIGN KEY (ingredient_id)"
                "    REFERENCES ingredients(ingredient_id),"
                "    CONSTRAINT fk_recipes FOREIGN KEY (recipe_id)"
                "    REFERENCES recipes(recipe_id)"
                ");")
    con.commit()
    recipe_name = input("Recipe name: ")
    recipe_id, serve_id, quantity_id = 0, 0, 0
    while recipe_name != "":
        recipe_description = input("Recipe description: ")
        cur.execute(f"INSERT INTO recipes VALUES ({recipe_id},"
                    f"'{recipe_name}', '{recipe_description}');")
        con.commit()
        all_rows = cur.execute("SELECT * FROM meals;").fetchall()
        for row in all_rows:
            print(f"{row[0]}) {row[1]}  ", end="")
        print()
        nums = [int(n) for n in input("When the dish can be served: ").split()]
        for num in nums:
            cur.execute(f"INSERT INTO serve VALUES ({serve_id}, {recipe_id},"
                        f"{num});")
            serve_id += 1
        con.commit()
        while True:
            ingredient = input("Input quantity of ingredient <press enter to "
                               "stop>: ").split()
            if not ingredient:
                break
            q, m, i = 0, "", ""
            if len(ingredient) == 2:
                q, i = ingredient
            else:
                q, m, i = ingredient
            m_rows = cur.execute(f"SELECT measure_id FROM measures "
                                 f"WHERE measure_name LIKE '{m}%';").fetchall()
            if len(m_rows) != 1:
                print("The measure is not conclusive!")
                continue
            i_rows = cur.execute(f"SELECT ingredient_id FROM ingredients WHERE "
                                 f"ingredient_name LIKE '%{i}%';").fetchall()
            if len(i_rows) != 1:
                print("The ingredient is not conclusive!")
                continue
            cur.execute(f"INSERT INTO quantity VALUES ({quantity_id}, "
                        f"{m_rows[0][0]}, {i_rows[0][0]}, {q}, {recipe_id});")
            quantity_id += 1
        con.commit()
        recipe_id += 1
        recipe_name = input("Recipe name: ")
    con.commit()
    con.close()


if __name__ == "__main__":
    main()
