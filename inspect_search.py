from bs4 import BeautifulSoup

with open("search_page.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "lxml")

titles = soup.select("p.name.product-title.woocommerce-loop-product__title")

print(f"Found {len(titles)} product titles:\n")

for i, title in enumerate(titles, start=1):
    print(f"{i}. {title.get_text(strip=True)}")