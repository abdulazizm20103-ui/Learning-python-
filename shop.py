import sqlite3


class Shop:
    def __init__(self):
        self.conn = sqlite3.connect("shop.db")
        self.cursor = self.conn.cursor()


        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                quantity INTEGER,
                category TEXT
            )
        """)
        self.conn.commit()

    def add_product(self, name, price, quantity, category):
        self.cursor.execute(
            "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
            (name, price, quantity, category)
        )
        self.conn.commit()
        print("Товар добавлен")

    def remove_product(self, name):
        self.cursor.execute(
            "DELETE FROM products WHERE name = ?",
            (name,)
        )
        self.conn.commit()
        print("Если товар был — он удалён")

    def show_all(self):
        self.cursor.execute("SELECT name, price, quantity, category FROM products")
        rows = self.cursor.fetchall()

        if not rows:
            print("Склад пуст")
            return

        for row in rows:
            name, price, quantity, category = row
            total = price * quantity

            print(f"Название: {name}")
            print(f"Цена: {price}")
            print(f"Количество: {quantity}")
            print(f"Категория: {category}")
            print(f"Общая стоимость: {total}")
            print("----------------------")

    def total_sum(self):
        self.cursor.execute(
            "SELECT SUM(price * quantity) FROM products"
        )
        result = self.cursor.fetchone()[0]

        return result if result else 0

    def find_by_category(self, category):
        self.cursor.execute(
            "SELECT name, price, quantity FROM products WHERE category = ?",
            (category,)
        )
        rows = self.cursor.fetchall()

        if not rows:
            print("Нет товаров в этой категории")
            return

        for row in rows:
            print(f"{row[0]} | цена: {row[1]} | кол-во: {row[2]}")

    def close(self):
        self.conn.close()




shop = Shop()

while True:
    print("\n1-добавить 2-удалить 3-показать 4-сумма 5-категория 6-выход")
    a = input("Выбор: ")

    if a == "1":
        name = input("Название: ")
        price = float(input("Цена: "))
        quantity = int(input("Количество: "))
        category = input("Категория: ")

        shop.add_product(name, price, quantity, category)

    elif a == "2":
        name = input("Удалить: ")
        shop.remove_product(name)

    elif a == "3":
        shop.show_all()

    elif a == "4":
        print("Сумма склада:", shop.total_sum())

    elif a == "5":
      category = input("Введите категорию: ")
      shop.find_by_category (category)


    elif a == "6":
      shop.close()
      print("Выход...")
      break

    else:
        print("Неверный выбор")
