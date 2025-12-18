import sqlite3

def create_database():
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        release_year INTEGER,
        price REAL
    )
    ''')
    
    games = [
        ('The Witcher 3', 'RPG', 2015, 39.99),
        ('Cyberpunk 2077', 'RPG', 2020, 59.99),
        ('Minecraft', 'Sandbox', 2011, 26.95),
        ('Grand Theft Auto V', 'Action', 2013, 29.99),
        ('Red Dead Redemption 2', 'Action', 2018, 59.99)
    ]
    
    cursor.executemany('''
    INSERT INTO games (title, genre, release_year, price) 
    VALUES (?, ?, ?, ?)
    ''', games)
    
    conn.commit()
    conn.close()
    
    print("games.db created")

create_database()