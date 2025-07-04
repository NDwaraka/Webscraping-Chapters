# Should be run only after cha_pyw_crfold is run i.e there are html files at the outputdir

import json
import os
import re


def extract_number(title):
    # Extract first number found in title or 0 if none
    match = re.search(r'\d+', title)
    return int(match.group()) if match else 0

def is_side_story(title):
    # Check if title contains 'Side Story' or similar
    return 'side story' in title.lower()


# OUTPUT_DIR = r"C:\Users\Lenovo\Documents\pers_proj/DamnHunterLife"
OUTPUT_DIR = r"C:\Users\Lenovo\Documents\pers_proj/paywall/DamnHunterLife"

chapters_manifest = []

# List HTML files and build manifest
for file in sorted(os.listdir(OUTPUT_DIR)):
    if file.endswith(".html"):
        title = os.path.splitext(file)[0].replace("_", " ")  # crude title extraction
        chapters_manifest.append({
            "title": title,
            # "filename": f"../DamnHunterLife/{file}"
            "filename": f"DamnHunterLife/{file}"
        })
        
# sort the list in-place by extracted number from title
chapters_manifest.sort(key=lambda chap: (
    is_side_story(chap["title"]),    # False for main chapters, True for side stories
    extract_number(chap["title"])    # Then by number
))

# Save chapters.json
with open("chapters.json", "w", encoding="utf-8") as f:
    json.dump(chapters_manifest, f, indent=2)

print("✅ Saved manifest file: chapters.json with", len(chapters_manifest), "chapters.")