import sqlite3
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def setup_database():
    print("Creating database and tables...")
    conn = sqlite3.connect('articles.db')
    with open('lib/db/schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database schema created.")
    from lib.db.seed import seed_data
    seed_data()

if __name__ == "__main__":
    setup_database()