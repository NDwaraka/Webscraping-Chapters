import json
import os


OUTPUT_DIR = r"C:\Users\Lenovo\Documents\pers_proj/DamnHunterLife"

chapters_manifest = []

# Save chapters.json
with open(os.path.join(OUTPUT_DIR, "chapters.json"), "w", encoding="utf-8") as f:
    json.dump(chapters_manifest, f, indent=2)

print("✅ Saved manifest file: chapters.json")