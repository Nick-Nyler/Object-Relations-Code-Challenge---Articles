# Articles Code Challenge

A Python application modeling Authors, Articles, and Magazines with a SQLite database using raw SQL queries.

## Setup

1. **Create virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  
   ```
2. **Install dependencies**:
   ```bash
     pip install pytest
     ```
3. **Setup database**:
    ```bash
     python scripts/setup_db.py
     ```
4. **Run tests**:
   ```bash
     pytest
     ```
5. **Debug interactively**:
   ```bash
     python lib/debug.py
     ```
6. **Run CLI tool**:
    ```bash
      python scripts/run_queries.py
      ```

## Features
Author, Article, and Magazine classes with SQL-based CRUD operations
Relationship methods for articles, magazines, and authors
Transaction handling and error management
Comprehensive test suite
CLI tool for interactive querying
Optimized SQL queries with indexes

## Database Schema
authors: id, name
magazines: id, name, category
articles: id, title, author_id, magazine_id    


#### 13. Git Commit Sequence

Follow the recommended commit sequence:

```bash
git init
git add README.md .gitignore
git commit -m "Initialize project structure and documentation"

git add lib/db/connection.py lib/db/schema.sql
git commit -m "Add database connection and schema"

git add lib/models/author.py
git commit -m "Implement Author class with SQL methods"

git add lib/models/magazine.py
git commit -m "Implement Magazine class with SQL methods"

git add lib/models/article.py
git commit -m "Implement Article class with SQL methods"

git add lib/db/seed.py scripts/setup_db.py
git commit -m "Add seed data and database setup script"

git add tests/
git commit -m "Add test suite for all models"

git add lib/debug.py scripts/run_queries.py
git commit -m "Add debug script and CLI tool"

git add .
git commit -m "Final documentation and cleanup"