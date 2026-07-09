import requests


class EngineDenAPI:
    """
    Handles communication with the EngineDen AJAX API.
    """

    BASE_URL = (
        "https://engineden.co.za/wp-admin/admin-ajax.php"
    )

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        ),
        "Referer": "https://engineden.co.za/",
        "X-Requested-With": "XMLHttpRequest",
    }

    def search(self, query: str) -> list:

        response = requests.get(
            self.BASE_URL,
            params={
                "action": "flatsome_ajax_search_products",
                "query": query,
            },
            headers=self.HEADERS,
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("suggestions", [])