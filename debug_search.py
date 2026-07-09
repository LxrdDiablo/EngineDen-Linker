from urllib.parse import quote

import requests

url = (
    "https://engineden.co.za/?s="
    + quote("Toyota 2KD Engine")
    + "&post_type=product"
)

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

with open("search_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved search_page.html")