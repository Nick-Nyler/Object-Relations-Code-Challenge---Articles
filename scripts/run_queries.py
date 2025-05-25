import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def cli():
    while True:
        print("\n1. List all authors")
        print("2. List all magazines")
        print("3. List all articles")
        print("4. Find author by name")
        print("5. Find magazine by name")
        print("6. Add new article")
        print("7. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            for row in cursor.fetchall():
                print(dict(row))
            conn.close()
        
        elif choice == "2":
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM magazines")
            for row in cursor.fetchall():
                print(dict(row))
            conn.close()
        
        elif choice == "3":
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articles")
            for row in cursor.fetchall():
                print(dict(row))
            conn.close()
        
        elif choice == "4":
            name = input("Enter author name: ")
            author = Author.find_by_name(name)
            print(f"Author: {author.name if author else 'Not found'}")
        
        elif choice == "5":
            name = input("Enter magazine name: ")
            magazine = Magazine.find_by_name(name)
            print(f"Magazine: {magazine.name if magazine else 'Not found'}")
        
        elif choice == "6":
            title = input("Enter article title: ")
            author_name = input("Enter author name: ")
            magazine_name = input("Enter magazine name: ")
            author = Author.find_by_name(author_name) or Author(author_name)
            magazine = Magazine.find_by_name(magazine_name) or Magazine(magazine_name, "General")
            article = author.add_article(magazine, title)
            print(f"Article '{article.title}' added successfully")
        
        elif choice == "7":
            break

if __name__ == "__main__":
    cli()