import cmd
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def add_author_with_articles(author_name, articles_data):
    conn = get_connection()
    try:
        conn.execute("BEGIN TRANSACTION")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO authors (name) VALUES (?) RETURNING id",
            (author_name,)
        )
        author_id = cursor.fetchone()[0]
        for article in articles_data:
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (article['title'], author_id, article['magazine_id'])
            )
        conn.execute("COMMIT")
        return True
    except Exception as e:
        conn.execute("ROLLBACK")
        print(f"Transaction failed: {e}")
        return False
    finally:
        conn.close()

class ArticleCLI(cmd.Cmd):
    prompt = "(Articles CLI) "

    def do_authors(self, arg):
        authors = Author.find_by_name(arg) or Author.find_by_id(int(arg)) if arg else []
        if authors:
            print(authors.name, authors.articles())
        else:
            print("Author not found")

    def do_quit(self, arg):
        return True

if __name__ == "__main__":
    ArticleCLI().cmdloop()