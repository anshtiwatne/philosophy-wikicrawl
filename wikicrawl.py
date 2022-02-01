"""
WIP
"""

# Rules:
# 1. Clicking on the first non-parenthesized, non-italicized link
# 2. Ignoring external links, links to the current page, or red links
# 3. Stopping when: reaching "Philosophy" / a page without links / if a loop occurs

from requests import get
import re

start_page = "/wiki/Wikipedia:Special:Random"
start_page = "/wiki/Elon_musk"

def get_first_link(wiki_page: str) -> str:
    html = get("https://wikipedia.org" + wiki_page).text
    href = re.search(r"<p>.*?href=\"(\/wiki\/[^:]*?)\"", html)[1]
    return href

wiki_page = start_page
while wiki_page != "/wiki/Philosophy":
    wiki_page = get_first_link(wiki_page)
    print(wiki_page)