import os
import http.server
import socketserver
import threading
import shutil
import requests
from tqdm import tqdm
import time

# Start local HTTP server to serve HTML files
PORT = 5501
Handler = http.server.SimpleHTTPRequestHandler

# Change directory to OUTPUT_DIR to serve files from there
OUTPUT_DIR = r"C:\Users\Lenovo\Documents\pers_proj/DamnHunterLifeTemp"  # 🔁 Your custom folder
os.chdir(OUTPUT_DIR)

DOWNLOAD_DIR = r"C:\Users\Lenovo\Documents\pers_proj/DamnHunterLife"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://127.0.0.1:{PORT}")
        httpd.serve_forever()

# Run server in background thread
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Wait for the server to spin up
time.sleep(1)

# List of HTML files created
html_files = [f for f in os.listdir() if f.endswith(".html")]

# Now download each served HTML file to FINAL_DOWNLOAD_DIR
for html_file in tqdm(html_files, desc="Downloading served HTML files"):
    file_url = f"http://127.0.0.1:{PORT}/{html_file}"
    try:
        r = requests.get(file_url)
        r.raise_for_status()

        final_path = os.path.join(DOWNLOAD_DIR, html_file)
        with open(final_path, "wb") as f:
            f.write(r.content)
    except Exception as e:
        print(f"Failed to download {file_url}: {e}")

print("\n✅ All files downloaded.")

# Shutdown server (will automatically close with main thread since it's daemon)

# Clean up the temp folder
os.chdir("..")  # go back so we can delete OUTPUT_DIR
shutil.rmtree(OUTPUT_DIR)
print(f"🗑️ Deleted temporary folder: {OUTPUT_DIR}")
