import requests
from bs4 import BeautifulSoup
import os

# Constants
URL = ""
HEADERS = {""}
API_ENDPOINT = ""
TEMPLATE_FILE = "template.html"
OUTPUT_DIR = r""  # 🔁 Your custom folder

# Load the HTML template
with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
    html_template = f.read()

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# [Step 1: Scrape page_ids and chapter_links remains unchanged]

response = requests.get(URL, headers=HEADERS)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

page_ids = []
# chapter_links = []

eplist = soup.select("")

for li in eplist:
    data_id = li.get("data-id")
    # a_tag = li.find("a")
    # href = a_tag["href"] if a_tag else None

    # if data_id and href:
    if data_id:
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

        title = post_data['title']['rendered']
        raw_html = post_data['content']['rendered']
        soup = BeautifulSoup(raw_html, "html.parser")
        cleaned_html = soup.prettify()

        final_html = html_template.replace("{{title}}", title).replace("{{content}}", cleaned_html)

        safe_title = "".join(c if c.isalnum() or c in " -_()" else "_" for c in title)
        filename = os.path.join(OUTPUT_DIR, f"{safe_title}.html")  # 🔁 Save in custom folder

        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_html)

        print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error fetching post {data_id}: {e}")
