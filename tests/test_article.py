import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_data
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    from scripts.setup_db import setup_database
    setup_database()
    yield

def test_article_save(setup_db):
    author = Author("Test Author")
    author.save()
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    
    article = Article("Test Article", author.id, magazine.id)
    article.save()
    retrieved = Article.find_by_id(article.id)
    assert retrieved is not None, "Failed to retrieve saved article"
    assert retrieved.title == "Test Article"
    assert retrieved.author_id == author.id
    assert retrieved.magazine_id == magazine.id

def test_article_author(setup_db):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM articles LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if not row:
        pytest.skip("No articles found in seed data")
    article = Article.find_by_id(row['id'])
    author = article.author()
    assert author is not None, "No author found for article"
    assert author.id == article.author_id

def test_article_magazine(setup_db):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM articles LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if not row:
        pytest.skip("No articles found in seed data")
    article = Article.find_by_id(row['id'])
    magazine = article.magazine()
    assert magazine is not None, "No magazine found for article"
    assert magazine.id == article.magazine_id