from core.browser import BrowserManager

browser = BrowserManager()

browser.start(headless=True)

browser.open(
    "https://engineden.co.za/?s=Toyota+2KD+Engine&post_type=product"
)

html = browser.page_source()

print(len(html))

browser.close()