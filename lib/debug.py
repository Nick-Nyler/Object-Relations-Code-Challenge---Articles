import os
import sys
import sqlite3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from scripts.setup_db import setup_database

def inspect_database():
    conn = sqlite3.connect('articles.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("\nAuthors:")
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    if authors:
        for row in authors:
            print(dict(row))
    else:
        print("No authors found.")

    print("\nMagazines:")
    cursor.execute("SELECT * FROM magazines")
    magazines = cursor.fetchall()
    if magazines:
        for row in magazines:
            print(dict(row))
    else:
        print("No magazines found.")

    print("\nArticles:")
    cursor.execute("SELECT * FROM articles")
    articles = cursor.fetchall()
    if articles:
        for row in articles:
            print(dict(row))
    else:
        print("No articles found.")

    conn.close()

if __name__ == "__main__":
    try:
        setup_database()
        print("Database initialized.")
        inspect_database()
        print("\nChecking specific records:")
        author = Author.find_by_id(1)
        print(f"Author ID 1: {author.name if author else None}")
        article = Article.find_by_id(1)
        print(f"Article ID 1: {article.title if article else None}")
        magazine = Magazine.find_by_id(1)
        print(f"Magazine ID 1: {magazine.name if magazine else None}")
    except Exception as e:
        print(f"Error: {e}")