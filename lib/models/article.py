from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self._title = None
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # Verify author_id and magazine_id exist
            cursor.execute("SELECT id FROM authors WHERE id = ?", (self.author_id,))
            if not cursor.fetchone():
                raise ValueError(f"Author with ID {self.author_id} does not exist")
            cursor.execute("SELECT id FROM magazines WHERE id = ?", (self.magazine_id,))
            if not cursor.fetchone():
                raise ValueError(f"Magazine with ID {self.magazine_id} does not exist")

            if self.id is None:
                cursor.execute(
                    "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?) RETURNING id",
                    (self.title, self.author_id, self.magazine_id)
                )
                self.id = cursor.fetchone()['id']
                conn.commit()
            else:
                cursor.execute(
                    "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                    (self.title, self.author_id, self.magazine_id, self.id)
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
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row['title'], row['author_id'], row['magazine_id'], row['id']) if row else None

    def author(self):
        from .author import Author
        return Author.find_by_id(self.author_id)

    def magazine(self):
        from .magazine import Magazine
        return Magazine.find_by_id(self.magazine_id)