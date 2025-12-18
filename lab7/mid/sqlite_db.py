import sqlite3
import os

def create_database():
    task_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(task_dir,"games.db")

    conn = sqlite3.connect(db_dir)
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
        ('The Witcher 3', 'RPG', 2015, 40),
        ('Cyberpunk 2077', 'RPG', 2020, 60),
        ('Minecraft', 'Sandbox', 2011, 27),
        ('Grand Theft Auto V', 'Action', 2013, 30),
        ('Red Dead Redemption 2', 'Action', 2018, 60)
    ]
    
    cursor.executemany('''
    INSERT INTO games (title, genre, release_year, price) 
    VALUES (?, ?, ?, ?)
    ''', games)
    
    conn.commit()
    conn.close()
    
    print("games.db created")

create_database()