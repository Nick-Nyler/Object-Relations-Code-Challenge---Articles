import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.seed import seed_database

def main():
    from scripts.setup_db import setup_database
    setup_database()
    
    author = Author.find_by_name("John Doe")
    print(f"Author: {author.name}")
    print(f"Articles: {author.articles()}")
    print(f"Magazines: {author.magazines()}")
    print(f"Topic Areas: {author.topic_areas()}")
    
    magazine = Magazine.find_by_name("Tech Weekly")
    print(f"\nMagazine: {magazine.name}")
    print(f"Articles: {magazine.articles()}")
    print(f"Contributors: {magazine.contributors()}")
    print(f"Article Titles: {magazine.article_titles()}")
    
    top_mag = Magazine.top_publisher()
    print(f"\nTop Publisher: {top_mag.name if top_mag else 'None'}")

if __name__ == "__main__":
    main()