import requests
from bs4 import BeautifulSoup

# Target URL
URL = "https://hyacinthbloom.com/series/shitty-hunter-life/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Arrays to store data
page_ids = []
chapter_links = []

# Fetch and parse the page
response = requests.get(URL, headers=HEADERS)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Traverse to the <ul> inside .eplister
eplist = soup.select("div.mainholder div.sertwofull div.postbody article div.sertobody div.bixbox div.eplister ul li")

for li in eplist:
    data_id = li.get("data-id")
    a_tag = li.find("a")
    href = a_tag["href"] if a_tag else None

    if data_id and href:
        page_ids.append(data_id)
        chapter_links.append(href)

# Reverse the arrays
page_ids.reverse()
chapter_links.reverse()

# Output the results
print("Page IDs:")
print(page_ids)
print("\nChapter Links:")
print(chapter_links)
