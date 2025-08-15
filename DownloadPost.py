import os
import requests
from bs4 import BeautifulSoup
from random import choice
from urllib.parse import quote_plus

# Expanded keyword list
keywords = [
    "cars", "watches", "anime", "technology", "landscapes", "minimalist art", 
    "coding memes", "sci-fi", "fantasy warriors", "streetwear fashion", "cyberpunk"
]

# Check if list is empty
if not keywords:
    raise ValueError("Keyword list is empty. Please add some search terms.")

# Choose random keyword and encode it
selected_keyword = choice(keywords)
encoded_keyword = quote_plus(selected_keyword)

# Construct search URL
SEARCH_URL = f"https://www.pinterest.com/search/pins/?q={encoded_keyword}&rs=typed"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
SAVE_DIR = "posts"

# Ensure posts folder exists
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Fetch the page
response = requests.get(SEARCH_URL, headers=HEADERS)
if response.status_code != 200:
    print("Failed to fetch page")
    exit()

# Parse the page
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

# Find all image tags
img_tags = soup.find_all("img")
count = 0
for img in img_tags:
    img_url = img.get("src") or img.get("data-src")
    if img_url and "pinimg.com" in img_url:
        try:
            img_data = requests.get(img_url, timeout=10).content
            with open(f"{SAVE_DIR}/image_{count}.jpg", "wb") as f:
                f.write(img_data)
            print(f"Downloaded image_{count}.jpg")
            count += 1
        except Exception as e:
            print(f"Failed to download image: {e}")

print(f"Downloaded {count} images to '{SAVE_DIR}'")
