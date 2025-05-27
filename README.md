# Articles Code Challenge

A Python application modeling Authors, Articles, and Magazines with a SQLite database using raw SQL queries. This project implements object-oriented programming principles, raw SQL operations, and proper database relationships without using SQLAlchemy.

## Project Overview

This project models a many-to-many relationship between `Authors`, `Articles`, and `Magazines`:
- An `Author` can write many `Articles`.
- A `Magazine` can publish many `Articles`.
- An `Article` belongs to both an `Author` and a `Magazine`.
- The `Author`-`Magazine` relationship is many-to-many through the `Articles` table.

The application uses SQLite for data persistence, includes a comprehensive test suite, and provides a CLI tool for interactive querying.

## Features
* Author, Article, and Magazine classes with SQL-based CRUD operations
* Relationship methods for articles, magazines, and authors
* Transaction handling and error management
* Comprehensive test suite
* CLI tool for interactive querying
* Optimized SQL queries with indexes

## Database Schema
* authors: id, name
* magazines: id, name, category
* articles: id, title, author_id, magazine_id    

## Setup Instructions

### Prerequisites
- Python 3.8+
- `pip` for installing dependencies
- Git for version control

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
* Author, Article, and Magazine classes with SQL-based CRUD operations
* Relationship methods for articles, magazines, and authors
* Transaction handling and error management
* Comprehensive test suite
* CLI tool for interactive querying
* Optimized SQL queries with indexes

## Database Schema
* authors: id, name
* magazines: id, name, category
* articles: id, title, author_id, magazine_id    
