import requests
from bs4 import BeautifulSoup

# Load the HTML template from file
with open("template.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# URL of the WordPress JSON post
url = "https://hyacinthbloom.com/wp-json/wp/v2/posts/27677"

# Fetch the JSON data
response = requests.get(url)
data = response.json()

# Extract title
title = data['title']['rendered']

# Extract and clean HTML content
html_content = data['content']['rendered']
soup = BeautifulSoup(html_content, "html.parser")

# text_content = soup.get_text()
# Print plain text
# print(text_content)

clean_html = soup.prettify()

# Replace placeholders in the template
final_html = html_template.replace("{{title}}", title).replace("{{content}}", clean_html)

# Write to output file
filename = f"{title}.html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(final_html)

print("HTML file generated as 'post_output.html'.")