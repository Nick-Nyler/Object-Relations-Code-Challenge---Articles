import pytest
from lib.models.magazine import Magazine
from lib.db.seed import seed_data
from lib.db.connection import get_connection

@pytest.fixture
def setup_db():
    from scripts.setup_db import setup_database
    setup_database()
    yield

def test_magazine_save(setup_db):
    magazine = Magazine("Test Magazine", "Test Category")
    magazine.save()
    retrieved = Magazine.find_by_name("Test Magazine")
    assert retrieved is not None
    assert retrieved.name == "Test Magazine"
    assert retrieved.category == "Test Category"

def test_magazine_articles(setup_db):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM magazines LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if not row:
        pytest.skip("No magazines found in seed data")
    magazine = Magazine.find_by_id(row['id'])
    articles = magazine.articles()
    assert len(articles) >= 2, f"Expected at least 2 articles for magazine ID {magazine.id}"
    assert all(article.magazine_id == magazine.id for article in articles)

def test_magazine_contributors(setup_db):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM magazines LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if not row:
        pytest.skip("No magazines found in seed data")
    magazine = Magazine.find_by_id(row['id'])
    contributors = magazine.contributors()
    assert len(contributors) >= 1, f"Expected at least 1 contributor for magazine ID {magazine.id}"