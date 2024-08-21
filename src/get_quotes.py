from db import create_connection, get_quotes_by_author


def main():
    # Database file
    db_file = "../database/quotes.db"

    # Create a database connection
    conn = create_connection(db_file)

    # Prompt the user for the author's name
    default_author = "Albert Einstein"
    author_name = (
        input(f"Enter the author's name (default: {default_author}): ")
        or default_author
    )

    # Get quotes by the author
    quotes = get_quotes_by_author(conn, author_name)

    # Print the quotes
    if quotes:
        print(f"Quotes by {author_name}:")
        for quote in quotes:
            print(f"- {quote[0]}")
    else:
        print(f"No quotes found for author: {author_name}")

    # Close the database connection
    conn.close()


if __name__ == "__main__":
    main()
