from PySide6.QtGui import QColor
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

    items = [

        QTableWidgetItem(product.matched_name),

        QTableWidgetItem(str(product.confidence)),

        QTableWidgetItem(product.status),

        QTableWidgetItem(product.engineden_url)

    ]

    for column, item in enumerate(items, start=1):

        self.setItem(row, column, item)

    # -------------------------
    # Row Colours
    # -------------------------

    if product.status == "Found":

        if product.confidence >= 95:

            colour = QColor(210, 255, 210)      # Green

        elif product.confidence >= 80:

            colour = QColor(255, 255, 190)      # Yellow

        else:

            colour = QColor(255, 225, 180)      # Orange

    else:

        colour = QColor(255, 210, 210)          # Red

    for col in range(self.columnCount()):

        cell = self.item(row, col)

        if cell:

            cell.setBackground(colour)

    def clear_results(self):

        self.setRowCount(0)