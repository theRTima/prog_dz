import sqlite3
import csv
from datetime import datetime

def export_to_csv():
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()
  
    cursor.execute('PRAGMA table_info(games)')
    columns = [column[1] for column in cursor.fetchall()]
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'games_export_{timestamp}.csv'
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
    
        writer.writerow(columns)

        writer.writerows(games)
    
    readable_filename = f'games_readable_{timestamp}.csv'
    
    with open(readable_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerow(['ID', 'Название', 'Жанр', 'Год выхода', 'Цена (USD)'])
        
        for game in games:
            writer.writerow([
                game[0],
                game[1],
                game[2],
                game[3],
                f"${game[4]:.2f}"
            ])
    
    conn.close()

    print("\nfirst 3 lines:")
    with open(readable_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i < 4: 
                print(" | ".join(row))
            else:
                break

export_to_csv()