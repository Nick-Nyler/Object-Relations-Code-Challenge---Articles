import pytest
from lib.models.author import Author
from lib.db.seed import seed_data
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    from scripts.setup_db import setup_database
    setup_database()
    yield

def test_author_save(setup_db):
    author = Author("Test Author")
    author.save()
    retrieved = Author.find_by_name("Test Author")
    assert retrieved is not None
    assert retrieved.name == "Test Author"

def test_author_articles(setup_db):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM authors LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if not row:
        pytest.skip("No authors found in seed data")
    author = Author.find_by_id(row['id'])
    articles = author.articles()
    assert len(articles) >= 2, f"Expected at least 2 articles for author ID {author.id}"
    assert all(article.author_id == author.id for article in articles)

def test_author_magazines(setup_db):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM authors LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if not row:
        pytest.skip("No authors found in seed data")
    author = Author.find_by_id(row['id'])
    magazines = author.magazines()
    assert len(magazines) >= 1, f"Expected at least 1 magazine for author ID {author.id}"