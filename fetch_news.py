import os
import requests
import json
from datetime import datetime

# Get the API key from environment variables
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")

URL = "https://gnews.io/api/v4/top-headlines"
PARAMS = {
    "topic": "technology",
    "lang": "en",
    "token": API_KEY,  # Use the API key here
    "max": 10
}

# Fetch news
response = requests.get(URL, params=PARAMS)
if response.status_code == 200:
    data = response.json()

    # Extract relevant fields
    articles = [
        {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "image": article["image"],
            "publishedAt": article["publishedAt"]
        }
        for article in data.get("articles", [])
    ]

    # Save news to JSON file
    with open("news.json", "w") as file:
        json.dump({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "articles": articles
        }, file, indent=4)
    print("Tech news saved to news.json")
else:
    print(f"Failed to fetch news: {response.status_code}")