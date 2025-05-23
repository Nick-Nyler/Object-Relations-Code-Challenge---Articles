import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection
from lib.db.seed import seed_database

@pytest.fixture
def setup_database():
    from scripts.setup_db import setup_database
    setup_database()
    yield
    conn = get_connection()
    conn.execute("DROP TABLE articles")
    conn.execute("DROP TABLE authors")
    conn.execute("DROP TABLE magazines")
    conn.commit()
    conn.close()

def test_article_initialization(setup_database):
    author = Author("Test Author")
    magazine = Magazine("Test Mag", "Test Cat")
    article = Article("Test Article", author, magazine)
    assert article.title == "Test Article"
    assert article.author == author
    assert article.magazine == magazine
    assert article.id is not None

def test_article_validation(setup_database):
    author = Author("Test Author")
    magazine = Magazine("Test Mag", "Test Cat")
    with pytest.raises(ValueError):
        Article("", author, magazine)

def test_article_find_by_id(setup_database):
    author = Author("Test Author")
    magazine = Magazine("Test Mag", "Test Cat")
    article = Article("Test Article", author, magazine)
    found_article = Article.find_by_id(article.id)
    assert found_article.title == "Test Article"
    assert found_article.author.name == "Test Author"
    assert found_article.magazine.name == "Test Mag"