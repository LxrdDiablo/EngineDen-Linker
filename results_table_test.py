import sys

from PySide6.QtWidgets import QApplication

from gui.widgets.results_table import ResultsTable
from models.product import Product

app = QApplication(sys.argv)

table = ResultsTable()

products = [
    Product(
        row_number=2,
        description="Toyota 2KD Engine"
    ),
    Product(
        row_number=3,
        description="Mazda WL Engine"
    ),
]

table.load_products(products)

products[0].matched_name = "Toyota 2KD Hilux Engine"
products[0].confidence = 100
products[0].status = "Found"
products[0].engineden_url = "https://engineden.co.za/product/toyota-2kd-engine-hilux-used/"

table.update_product(products[0])

table.resize(1000, 300)
table.show()

app.exec()