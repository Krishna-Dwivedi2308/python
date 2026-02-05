"""
Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming languageYour task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Also:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"


def get_h2_headers(url):
    headers = {"User-Agent": "MyCoolDataBot/1.0 (contact@example.com)"}
    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()  # raises HTTP error if one occured.
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")  # find all h2 tags
    print(h2_tags)
    # the above line will print something like
    # [<h2 class="vector-pinnable-header-label">Contents</h2>, <h2 id="History">History</h2>, <h2 id="Design_philosophy_and_features">Design philosophy and features</h2>, <h2 id="Syntax_and_semantics">Syntax and semantics</h2>, <h2 id="Code_examples">Code examples</h2>, <h2 id="Libraries">Libraries</h2>, <h2 id="Development_environments">Development environments</h2>, <h2 id="Implementations">Implementations</h2>, <h2 id="Language_Development">Language Development</h2>, <h2 id="Naming">Naming</h2>, <h2 id="Languages_influenced_by_Python">Languages influenced by Python</h2>, <h2 id="See_also">See also</h2>, <h2 id="Notes">Notes</h2>, <h2 id="References">References</h2>, <h2 id="Further_reading">Further reading</h2>, <h2 id="External_links">External links</h2>]

    # now we need to read the above output and get the text from the h2 tags that we desire
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    # print(headers)


get_h2_headers(URL)
