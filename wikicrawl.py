"""
Script to automate the Wikipedia philosophy game

Rules:
1. Clicking on the first non-parenthesized, non-italicized link
2. Ignoring external links, links to the current page, or red links
3. Stopping when: reaching "Philosophy" / a page without links / if a loop occurs
"""

import re
import requests
import copy

START_PAGE = "/wiki/Wikipedia:Special:Random"
pages = set()


def get_first_link(wiki_page: str) -> str:
    """Get the first non-parenthesized, non-italicized link in the main body"""

    html = requests.get("https://wikipedia.org" + wiki_page).text
    href = re.search(r"<p>.*?href=\"(\/wiki\/[^:]*?)\"", html)[1]
    return href


def main():
    """Go to every first link and get a new one until it's /wiki/Philosophy """

    wiki_page = copy.copy(START_PAGE)
    i = 0

    while wiki_page != "/wiki/Philosophy":
        i += 1
        wiki_page = get_first_link(wiki_page)
        if wiki_page in pages:
            print("Stuck in a loop")
            break
        pages.add(wiki_page)
        print(f"{i}. {wiki_page}")


if __name__ == "__main__":
    main()
