import pytest
from lib.models.author import Author
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

def test_author_initialization(setup_database):
    author = Author("Test Author")
    assert author.name == "Test Author"
    assert author.id is not None

def test_author_validation(setup_database):
    with pytest.raises(ValueError):
        Author("")

def test_author_articles(setup_database):
    author = Author.find_by_name("John Doe")
    articles = author.articles()
    assert len(articles) >= 2
    assert any(article['title'] == "Tech Trends 2025" for article in articles)

def test_author_magazines(setup_database):
    author = Author.find_by_name("John Doe")
    magazines = author.magazines()
    assert any(mag['name'] == "Tech Weekly" for mag in magazines)
    assert any(mag['name'] == "Science Monthly" for mag in magazines)

def test_author_topic_areas(setup_database):
    author = Author.find_by_name("John Doe")
    categories = author.topic_areas()
    assert "Technology" in categories
    assert "Science" in categories