import requests

from bs4 import BeautifulSoup

url = (
    "https://engineden.co.za/wp-admin/admin-ajax.php"
)

params = {
    "action": "flatsome_ajax_search_products",
    "query": "Toyota 2KD Engine"
}

response = requests.get(
    url,
    params=params,
    headers={
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://engineden.co.za/"
    },
    timeout=30
)

print(response.status_code)

print()

print(response.text[:1000])