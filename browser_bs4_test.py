from bs4 import BeautifulSoup

from core.browser import BrowserManager

browser = BrowserManager()

browser.start(headless=False)   # Keep visible while testing

browser.open(
    "https://engineden.co.za/?s=Toyota+2KD+Engine&post_type=product"
)

html = browser.page_source()

print(f"Downloaded {len(html)} characters")

soup = BeautifulSoup(html, "lxml")

products = soup.select(
    "p.name.product-title.woocommerce-loop-product__title a"
)

print(f"\nFound {len(products)} products:\n")

for product in products:

    print(product.get_text(strip=True))

browser.close()