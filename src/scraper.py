import random
import requests
from bs4 import BeautifulSoup
import time


def scrape_quotes(base_url):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0"
    }

    page_number = 1
    scraped_data = []

    while True:
        try:
            response = session.get(f"{base_url}/page/{page_number}/", headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            # Catch HTTP errors
            print(f"HTTP error occurred: {http_err}")
            break
        except requests.exceptions.RequestException as req_err:
            # Catch other errors
            print(f"Request error occurred: {req_err}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quote_elements = soup.find_all("div", class_="quote")

        if not quote_elements:
            print("No more quotes found. Exiting.")
            break

        # Loop through each quote element and extract the quote, author, and tags
        for element in quote_elements:
            quote_text = element.find("span", class_="text").get_text()
            author_name = element.find("small", class_="author").get_text()
            quote_tags = [tag.get_text() for tag in element.find_all("a", class_="tag")]

            # Append the extracted data to the scraped_data list
            scraped_data.append(
                {
                    "quote_text": quote_text,
                    "author_name": author_name,
                    "tags": quote_tags,
                }
            )

        print(f"Page {page_number} scraped successfully.")
        page_number += 1

        # Sleep for a random duration between 1 and 2 seconds to avoid overwhelming the server
        time.sleep(random.uniform(1, 2))

    return scraped_data
