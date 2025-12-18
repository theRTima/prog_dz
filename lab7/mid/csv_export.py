import sqlite3
import csv
import os

def export_to_csv():
    task_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(task_dir,"games.db")

    conn = sqlite3.connect(db_dir)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()
  
    cursor.execute('PRAGMA table_info(games)')
    columns = [column[1] for column in cursor.fetchall()]
    
    filename = os.path.join(task_dir,"games.csv")
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        writer.writerows(games)
     
    conn.close()

    print("\nfirst 5 lines:")
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i < 6: 
                print(" | ".join(row))
            else:
                break

export_to_csv()