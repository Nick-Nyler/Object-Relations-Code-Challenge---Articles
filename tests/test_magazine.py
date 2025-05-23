import pytest
from lib.models.magazine import Magazine
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

def test_magazine_initialization(setup_database):
    magazine = Magazine("Test Mag", "Test Cat")
    assert magazine.name == "Test Mag"
    assert magazine.category == "Test Cat"
    assert magazine.id is not None

def test_magazine_validation(setup_database):
    with pytest.raises(ValueError):
        Magazine("", "Category")
    with pytest.raises(ValueError):
        Magazine("Name", "")

def test_magazine_articles(setup_database):
    magazine = Magazine.find_by_name("Tech Weekly")
    articles = magazine.articles()
    assert any(article['title'] == "Tech Trends 2025" for article in articles)

def test_magazine_contributors(setup_database):
    magazine = Magazine.find_by_name("Tech Weekly")
    contributors = magazine.contributors()
    assert any(contributor['name'] == "John Doe" for contributor in contributors)

def test_magazine_article_titles(setup_database):
    magazine = Magazine.find_by_name("Tech Weekly")
    titles = magazine.article_titles()
    assert "Tech Trends 2025" in titles
    assert "AI Revolution" in titles

def test_top_publisher(setup_database):
    top_mag = Magazine.top_publisher()
    assert top_mag.name == "Tech Weekly"