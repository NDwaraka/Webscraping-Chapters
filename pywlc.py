import requests
from bs4 import BeautifulSoup

# URL of the WordPress JSON post
url = "https://hyacinthbloom.com/wp-json/wp/v2/posts/27677"

# Fetch the JSON data
response = requests.get(url)
data = response.json()

# Extract and clean HTML content
html_content = data['content']['rendered']
soup = BeautifulSoup(html_content, "html.parser")
text_content = soup.get_text()

# Print plain text
print(text_content)
