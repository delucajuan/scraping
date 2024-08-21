import os
import subprocess
from db import (
    create_connection,
    insert_author,
    insert_quote,
    insert_tag,
    insert_quote_tag,
)
from scraper import scrape_quotes


def main():
    # URL to scrape
    base_url = "https://quotes.toscrape.com"
    # Database file
    db_file = "../database/quotes.db"

    # Check if the database file exists
    if not os.path.exists(db_file):
        print(f"{db_file} does not exist. Creating the database...")
        # Execute the create_db.py script to create the database
        subprocess.run(["python", "create_db.py"], check=True)
        print(f"{db_file} created successfully.")

    # Create a database connection
    conn = create_connection(db_file)

    try:
        # Scrape the data
        scraped_data = scrape_quotes(base_url)

        if not scraped_data:
            raise ValueError("No data scraped. Exiting.")

        # Save scraped data to the database
        for data in scraped_data:
            author_id = insert_author(conn, data["author_name"])
            quote_id = insert_quote(conn, data["quote_text"], author_id)
            for tag in data["tags"]:
                tag_id = insert_tag(conn, tag)
                insert_quote_tag(conn, quote_id, tag_id)

        print("✅ Scraping and saving to database completed successfully.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        # Close the database connection
        conn.close()


if __name__ == "__main__":
    main()
