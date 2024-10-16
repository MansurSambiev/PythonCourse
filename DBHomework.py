import sqlite3

conn = sqlite3.connect('shop.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
id INTEGER PRIMARY KEY,
name TEXT,
category TEXT,
price INT,
amount INT)
''')

conn.commit()
# Не писал close чтобы не комментировать каждый раз код перед выполнением следующей команды

cursor.execute("INSERT INTO items (name, category, price, amount) VALUES(?, ?, ?, ?)",
               ('ARDOR GAMING', 'игровая', 4099, 5))
conn.commit()

cursor.execute("INSERT INTO items (name, category, price, amount) VALUES(?, ?, ?, ?)",
               ('A4TECH', 'игровая', 2399, 8))
conn.commit()

cursor.execute("INSERT INTO items (name, category, price, amount) VALUES(?, ?, ?, ?)",
               ('Redragon Apas', 'игровая', 6499, 12))
conn.commit()

cursor.execute("INSERT INTO items (name, category, price, amount) VALUES(?, ?, ?, ?)",
               ('Logitech G413', 'игровая', 6999, 6))
conn.commit()

cursor.execute("INSERT INTO items (name, category, price, amount) VALUES(?, ?, ?, ?)",
               ('Ritmix', 'офисная', 650, 20))
conn.commit()

cursor.execute("INSERT INTO items (name, category, price, amount) VALUES(?, ?, ?, ?)",
               ('ExeGate', 'офисная', 1500, 10))
conn.commit()

cursor.execute("INSERT INTO items (name, category, price, amount) VALUES(?, ?, ?, ?)",
               ('Aceline', 'офисная', 850, 15))
conn.commit()

#Вывести все игровые клавиатуры дороже 5000р

cursor.execute("SELECT * FROM items WHERE category = 'игровая' AND price > 5000")
answer = cursor.fetchall()
print('Вывести все игровые клавиатуры дороже 5000р')
for i in answer:
    print(i)
conn.commit()

#Вывести все игровые клавиатуры дороже 2000р и с количеством больше 3
cursor.execute("SELECT * FROM items WHERE category = 'игровая' AND price > 2000 AND amount > 3")
answer = cursor.fetchall()
print('Вывести все игровые клавиатуры дороже 2000р и с количеством больше 3')
for i in answer:
    print(i)
conn.commit()

#Вывести все офисные клавиатуры дешевле 1000р
cursor.execute("SELECT * FROM items WHERE category = 'офисная' AND price < 1000")
answer = cursor.fetchall()
print('Вывести все офисные клавиатуры дешевле 1000р')
for i in answer:
    print(i)
conn.commit()

#Вывести офисную модель Exegate
cursor.execute("SELECT * FROM items WHERE category = 'офисная' AND name = 'ExeGate' ")
# или cursor.execute("SELECT * FROM items WHERE id = 6")
answer = cursor.fetchall()
print('Вывести офисную модель Exegate')
for i in answer:
    print(i)
conn.commit()
conn.close()