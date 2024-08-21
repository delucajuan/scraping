import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("../database/quotes.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the authors table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """
)

# Create the quotes table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quote_text TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY(author_id) REFERENCES authors(id)
    )
    """
)

# Create the tags table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tag TEXT NOT NULL
    )
    """
)

# Create the quote_tags table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS quote_tags (
        quote_id INTEGER,
        tag_id INTEGER,
        FOREIGN KEY(quote_id) REFERENCES quotes(id),
        FOREIGN KEY(tag_id) REFERENCES tags(id),
        PRIMARY KEY (quote_id, tag_id)
    )
    """
)

# Commit changes and close the connection
conn.commit()
conn.close()
