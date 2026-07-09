import requests

from bs4 import BeautifulSoup


class ProductPageParser:

    HEADERS = {
        "User-Agent": "Mozilla/5.0"
    }

    def get_full_image(self, product_url):

        response = requests.get(
            product_url,
            headers=self.HEADERS,
            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        image = soup.select_one(
            "img.wp-post-image"
        )

        if image is None:
            return ""

        return (
            image.get("data-src")
            or image.get("src")
            or ""
        )