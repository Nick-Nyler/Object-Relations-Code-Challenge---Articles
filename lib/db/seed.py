import sqlite3
from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()
    print("Clearing existing data...")
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='articles'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='authors'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='magazines'")
    conn.commit()
    
    print("Inserting authors...")
    authors = [
        ("John Doe",),
        ("Jane Smith",),
        ("Alice Johnson",)
    ]
    cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)
    conn.commit()
    cursor.execute("SELECT id FROM authors WHERE name IN ('John Doe', 'Jane Smith', 'Alice Johnson')")
    author_ids = [row['id'] for row in cursor.fetchall()]
    print(f"Author IDs: {author_ids}")
    
    print("Inserting magazines...")
    magazines = [
        ("Tech Weekly", "Technology"),
        ("Health Digest", "Health"),
        ("Science Monthly", "Science")
    ]
    cursor.executemany("INSERT INTO magazines (name, category) VALUES (?, ?)", magazines)
    conn.commit()
    cursor.execute("SELECT id FROM magazines WHERE name IN ('Tech Weekly', 'Health Digest', 'Science Monthly')")
    magazine_ids = [row['id'] for row in cursor.fetchall()]
    print(f"Magazine IDs: {magazine_ids}")
    
    print("Inserting articles...")
    articles = [
        ("Tech Trends 2025", author_ids[0], magazine_ids[0]),
        ("AI Revolution", author_ids[0], magazine_ids[0]),
        ("Healthy Living Tips", author_ids[1], magazine_ids[1]),
        ("Quantum Physics", author_ids[2], magazine_ids[2]),
        ("Data Science Insights", author_ids[0], magazine_ids[2])
    ]
    cursor.executemany("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", articles)
    conn.commit()
    
    print("Seed data inserted. Verifying...")
    cursor.execute("SELECT COUNT(*) FROM authors")
    print(f"Authors count: {cursor.fetchone()[0]}")
    cursor.execute("SELECT COUNT(*) FROM magazines")
    print(f"Magazines count: {cursor.fetchone()[0]}")
    cursor.execute("SELECT COUNT(*) FROM articles")
    print(f"Articles count: {cursor.fetchone()[0]}")
    conn.close()

if __name__ == "__main__":
    seed_data()