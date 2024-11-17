import sqlite3

conn = sqlite3.connect('base.db')

cursor = conn.cursor()

books = [
    ('Война и мир', 'Роман', 'Л.Н.Толстой', 1900),
    ('1984', 'Антиутопия', 'Джордж Оруэлл', 1949),
    ('Граф Монтекристо', 'Роман', 'Александр Дюма', 1846),
    ('Евгений Онегин', 'Поэма', 'А.С.Пушкин', 1833),
    ('Повелитель мух', 'Роман-Антиутопия', 'Уильяма Голдинг', 1954),
    ('Горе от ума', 'комедия', 'А.С.Грибоедов', 1862)
]

def createTable():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title VARCHAR(48) UNIQUE,
    genre VARCHAR(32),
    author VARCHAR(64),
    published_year INT
    )
    ''')
    conn.commit()


def insertTable():
    cursor.executemany("INSERT OR IGNORE INTO books (title, genre, author, published_year) VALUES(?, ?, ?, ?)", books)
    conn.commit()

def printBooks():
    print('Все книги')
    cursor.execute('SELECT * FROM books ORDER BY published_year')
    books = cursor.fetchall()
    for book in books:
        print(book)
    conn.commit()


def deleteFromTable(id):
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()


def updateTable(publ, id):
    cursor.execute("UPDATE books SET published_year = ? WHERE id = ?", (publ, id))
    conn.commit()


def getBooks(author):
    cursor.execute("SELECT * FROM books WHERE author = ?", (author,))
    request = cursor.fetchall()
    for req in request:
        print(req)
    conn.commit()

createTable()
insertTable()
deleteFromTable(3)
updateTable(1830, 4)
getBooks('А.С.Пушкин')
printBooks()

conn.close()
