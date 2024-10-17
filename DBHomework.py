import sqlite3

conn = sqlite3.connect('shop.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
id INTEGER PRIMARY KEY,
name VARCHAR(48) UNIQUE,
category VARCHAR(32),
price INT,
amount INT)
''')

conn.commit()
items = [
    ('ARDOR GAMING', 'игровая', 4099, 5),
    ('A4TECH', 'игровая', 2399, 8),
    ('Redragon Apas', 'игровая', 6499, 12),
    ('Logitech G413', 'игровая', 6999, 6),
    ('Ritmix', 'офисная', 650, 20),
    ('ExeGate', 'офисная', 1500, 10),
    ('Aceline', 'офисная', 850, 15)
]

# Не писал close чтобы не комментировать каждый раз код перед выполнением следующей команды

cursor.executemany("INSERT OR IGNORE INTO items (name, category, price, amount) VALUES(?, ?, ?, ?)", items)
conn.commit()

def selectFromTable(condition1, condition2):
    cursor.execute("SELECT * FROM items WHERE category = ? AND price > ?", (condition1, condition2))
    answer = cursor.fetchall()
    for i in answer:
        print(i)
    conn.commit()

#Не узнал как можно передать знак сравнения в функцию, пришлось создать еще одну функцию с измененным знаком с > на <
def selectCheaper(condition1, condition2):
    cursor.execute("SELECT * FROM items WHERE category = ? AND price < ?", (condition1, condition2))
    answer = cursor.fetchall()
    for i in answer:
        print(i)
    conn.commit()


print('Вывести все игровые клавиатуры дороже 5000р')
selectFromTable('игровая', 5000)

print('Вывести все игровые клавиатуры дороже 2000р и с количеством больше 3')
selectFromTable('игровая', 2000)

print('Вывести все офисные клавиатуры дешевле 1000р')
selectCheaper('офисная', 1000)

cursor.execute("SELECT * FROM items WHERE category = 'офисная' AND name = 'ExeGate' ")
# или cursor.execute("SELECT * FROM items WHERE id = 6")
answer = cursor.fetchall()
print('Вывести офисную модель Exegate')
for i in answer:
    print(i)
conn.commit()
conn.close()
