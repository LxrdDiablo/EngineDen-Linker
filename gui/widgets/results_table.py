from PySide6.QtWidgets import (
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
)


class ResultsTable(QTableWidget):
    """
    Displays products and live search results.
    """

    HEADERS = [
        "Excel Product",
        "Matched Product",
        "Confidence",
        "Status",
        "EngineDen URL",
    ]

    def __init__(self):

        super().__init__()

        self.setColumnCount(len(self.HEADERS))
        self.setHorizontalHeaderLabels(self.HEADERS)

        header = self.horizontalHeader()

        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.Stretch)

    def load_products(self, products):

        self.setRowCount(len(products))

        for row, product in enumerate(products):

            self.setItem(row, 0, QTableWidgetItem(product.description))
            self.setItem(row, 1, QTableWidgetItem(""))
            self.setItem(row, 2, QTableWidgetItem(""))
            self.setItem(row, 3, QTableWidgetItem("Waiting"))
            self.setItem(row, 4, QTableWidgetItem(""))

    def update_product(self, product):

        row = product.row_number - 2

        if row < 0 or row >= self.rowCount():
            return

        self.setItem(
            row,
            1,
            QTableWidgetItem(product.matched_name)
        )

        self.setItem(
            row,
            2,
            QTableWidgetItem(str(product.confidence))
        )

        self.setItem(
            row,
            3,
            QTableWidgetItem(product.status)
        )

        self.setItem(
            row,
            4,
            QTableWidgetItem(product.engineden_url)
        )

    def clear_results(self):

        self.setRowCount(0)