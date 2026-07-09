from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserManager:

    def __init__(self):

        self.driver = None

    def start(self, headless=False):

        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--log-level=3")

        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

    def open(self, url):

        self.driver.get(url)

    def page_source(self):

        return self.driver.page_source

    def close(self):

        if self.driver:
            self.driver.quit()