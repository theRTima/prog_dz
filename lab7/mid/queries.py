import sqlite3
import os

def queries():
    task_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(task_dir,"games.db")

    conn = sqlite3.connect(db_dir)
    cursor = conn.cursor()

    print("\n   genre search")

    genre = 'RPG'
    cursor.execute('SELECT * FROM games WHERE genre = ?', (genre,))
    rpg_games = cursor.fetchall()
    
    print(f"{genre} games:")
    for game in rpg_games:
        print(f"{game[1]} ({game[2]})")
    
    print("\n   Price filter")

    min_price = 30
    max_price = 60
    cursor.execute('''
    SELECT * FROM games 
    WHERE price BETWEEN ? AND ?
    ORDER BY price DESC
    ''', (min_price, max_price))
    
    filtered_games = cursor.fetchall()
    print(f"games for ${min_price} to ${max_price}:")
    for game in filtered_games:
        print(f"{game[1]} ${game[4]}")
    
    print("\n   game add")

    new_game = ('Elden Ring', 'RPG', 2022, 60)
    cursor.execute('''
    INSERT INTO games (title, genre, release_year, price)
    VALUES (?, ?, ?, ?)
    ''', new_game)
    conn.commit()

    print(f"game '{new_game[0]}' added")
    
    conn.close()


queries()