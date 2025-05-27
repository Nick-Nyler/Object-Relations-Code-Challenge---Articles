from lib.db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id is None:
                cursor.execute(
                    "INSERT INTO authors (name) VALUES (?) RETURNING id",
                    (self.name,)
                )
                self.id = cursor.fetchone()[0]
                conn.commit()
            else:
                cursor.execute(
                    "UPDATE authors SET name = ? WHERE id = ?",
                    (self.name, self.id)
                )
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['id']) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['id']) if row else None

    def articles(self):
        from .article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM articles WHERE author_id = ?",
            (self.id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [Article(row['title'], row['author_id'], row['magazine_id'], row['id']) for row in rows]

    def magazines(self):
        from .magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
            """,
            (self.id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(row['name'], row['category'], row['id']) for row in rows]

    def add_article(self, magazine, title):
        from .article import Article
        article = Article(title, self.id, magazine.id)
        article.save()
        return article

    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
            """,
            (self.id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [row['category'] for row in rows]

    @classmethod
    def most_prolific_author(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT a.*, COUNT(art.id) as article_count FROM authors a
            LEFT JOIN articles art ON a.id = art.author_id
            GROUP BY a.id
            ORDER BY article_count DESC
            LIMIT 1
            """
        )
        row = cursor.fetchone()
        conn.close()
        return cls(row['name'], row['id']) if row else None