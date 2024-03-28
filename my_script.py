import requests
from bs4 import BeautifulSoup


def get_first_search_result_link(query):
    try:
        # Perform the Google search
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the search results page
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('a')

        # Extract and return the link of the first search result
        for result in search_results:
            link = result.get('href')
            if link.startswith('/url?q='):
                return link[7:].split('&')[0]

        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None


# Example usage:
query = "brofine medicine used for"
first_result_link = get_first_search_result_link(query)
if first_result_link:
    print("First search result link:", first_result_link)
else:
    print("No search results found.")
