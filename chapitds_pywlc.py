import requests
from bs4 import BeautifulSoup
import os

# Constants
URL = "https://hyacinthbloom.com/series/shitty-hunter-life/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
API_ENDPOINT = "https://hyacinthbloom.com/wp-json/wp/v2/posts/"
TEMPLATE_FILE = "template.html"

# Load the HTML template
with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    html_template = f.read()

# Step 1: Fetch and parse the chapter list
response = requests.get(URL, headers=HEADERS)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

page_ids = []
# chapter_links = []

eplist = soup.select("div.mainholder div.sertwofull div.postbody article div.sertobody div.bixbox div.eplister ul li")

for li in eplist:
    data_id = li.get("data-id")
    # a_tag = li.find("a")
    # href = a_tag["href"] if a_tag else None

    if data_id and href:
        page_ids.append(data_id)
        # chapter_links.append(href)

# Reverse to maintain correct order
page_ids.reverse()
# chapter_links.reverse()

# Step 2: Process each chapter
for data_id in page_ids:
    api_url = f"{API_ENDPOINT}{data_id}"
    print(f"Fetching post ID {data_id}...")

    try:
        res = requests.get(api_url, headers=HEADERS)
        res.raise_for_status()
        post_data = res.json()

        # Extract title and HTML content
        title = post_data['title']['rendered']
        raw_html = post_data['content']['rendered']
        soup = BeautifulSoup(raw_html, "html.parser")
        cleaned_html = soup.prettify()

        # Inject into template
        final_html = html_template.replace("{{title}}", title).replace("{{content}}", cleaned_html)

        # Clean filename
        safe_title = "".join(c if c.isalnum() or c in " -_()" else "_" for c in title)
        filename = f"{safe_title}.html"

        # Save HTML file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_html)

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error fetching post {data_id}: {e}")
