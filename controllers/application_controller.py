from services.excel_service import ExcelService
from services.engineden_service import EngineDenService
from core.browser import BrowserManager


class ApplicationController:

    def __init__(self, window):

        self.window = window

        self.browser = BrowserManager()
        self.excel = ExcelService()

        self.engineden = None

    def start(self, excel_file):

        self.window.status_label.setText(
            "Status: Starting browser..."
        )

        self.browser.start()

        self.engineden = EngineDenService(self.browser)

        self.window.status_label.setText(
            "Status: Loading Excel..."
        )

        products = self.excel.load_products(excel_file)

        return products

    def stop(self):

        self.browser.close()