import sqlite3
import os


def create_connection(db_file):
    # Create a db connection
    if not os.path.exists(db_file):
        raise FileNotFoundError(f"Database file '{db_file}' does not exist.")
    conn = sqlite3.connect(db_file)
    return conn


def insert_author(conn, name):
    # Insert a new author or get the existing one
    cursor = conn.cursor()
    # Check if the author exists
    cursor.execute("SELECT id FROM authors WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        # Return the existing author ID
        return result[0]

    # If the author not exist, insert it
    cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
    conn.commit()
    # Return the new author ID
    return cursor.lastrowid


def insert_quote(conn, quote_text, author_id):
    # Insert a new quote or get the existing one
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM quotes WHERE quote_text = ? AND author_id = ?",
        (quote_text, author_id),
    )
    result = cursor.fetchone()
    if result:
        return result[0]

    cursor.execute(
        "INSERT INTO quotes (quote_text, author_id) VALUES (?, ?)",
        (quote_text, author_id),
    )
    conn.commit()
    return cursor.lastrowid


def insert_tag(conn, tag):
    # Insert a new tag or get the existing one
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tags WHERE tag = ?", (tag,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("INSERT INTO tags (tag) VALUES (?)", (tag,))
    conn.commit()
    return cursor.lastrowid


def insert_quote_tag(conn, quote_id, tag_id):
    # Insert a quote-tag relationship if it doesn't exist
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM quote_tags WHERE quote_id = ? AND tag_id = ?", (quote_id, tag_id)
    )
    result = cursor.fetchone()
    if result:
        return

    cursor.execute(
        "INSERT INTO quote_tags (quote_id, tag_id) VALUES (?, ?)", (quote_id, tag_id)
    )
    conn.commit()


def get_quotes_by_author(conn, author_name):
    # Get the quotes for a specific author ignoring case
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT q.quote_text
        FROM quotes q
        JOIN authors a ON q.author_id = a.id
        WHERE LOWER(a.name) = LOWER(?)
        """,
        (author_name,),
    )

    quotes = cursor.fetchall()
    return quotes
