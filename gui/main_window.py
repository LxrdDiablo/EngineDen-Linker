from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QProgressBar,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)

from services.excel_service import ExcelService


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.products = []

        self.setWindowTitle("EngineDen Linker v1.0")
        self.resize(1100, 700)

        central = QWidget()
        self.setCentralWidget(central)

        self.main_layout = QVBoxLayout()
        central.setLayout(self.main_layout)

        self.build_header()
        self.build_file_panel()
        self.build_progress_panel()
        self.build_product_table()
        self.build_control_panel()

    def build_header(self):

        title = QLabel("EngineDen Linker")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        subtitle = QLabel("Milestone 4 - Excel Integration")

        self.main_layout.addWidget(title)
        self.main_layout.addWidget(subtitle)

    def build_file_panel(self):

        self.main_layout.addWidget(QLabel("Excel File"))

        layout = QHBoxLayout()

        self.excel_edit = QLineEdit()

        browse = QPushButton("Browse")
        browse.clicked.connect(self.select_excel)

        layout.addWidget(self.excel_edit)
        layout.addWidget(browse)

        self.main_layout.addLayout(layout)

        self.main_layout.addWidget(QLabel("Output Folder"))

        layout = QHBoxLayout()

        self.output_edit = QLineEdit()

        browse = QPushButton("Browse")
        browse.clicked.connect(self.select_output)

        layout.addWidget(self.output_edit)
        layout.addWidget(browse)

        self.main_layout.addLayout(layout)

    def build_progress_panel(self):

        self.main_layout.addWidget(QLabel("Progress"))

        self.progress_bar = QProgressBar()

        self.progress_bar.setValue(0)

        self.main_layout.addWidget(self.progress_bar)

        self.status_label = QLabel("Status: Waiting...")

        self.main_layout.addWidget(self.status_label)

    def build_product_table(self):

        self.main_layout.addWidget(QLabel("Products"))

        self.product_table = QTableWidget()

        self.product_table.setColumnCount(4)

        self.product_table.setHorizontalHeaderLabels([
            "Product",
            "Status",
            "Confidence",
            "EngineDen URL",
        ])

        self.main_layout.addWidget(self.product_table)

    def build_control_panel(self):

        layout = QHBoxLayout()

        layout.addStretch()

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")

        self.stop_button.setEnabled(False)

        self.start_button.clicked.connect(self.load_excel)

        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)

        self.main_layout.addLayout(layout)

    def load_excel(self):

        filename = self.excel_edit.text()

        if filename == "":

            QMessageBox.warning(
                self,
                "No Excel File",
                "Please select an Excel workbook."
            )

            return

        try:

            service = ExcelService()

            self.products = service.load_products(filename)

            self.populate_table()

            self.progress_bar.setValue(100)

            self.status_label.setText(
                f"Status: Loaded {len(self.products)} products."
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    def populate_table(self):

        self.product_table.setRowCount(len(self.products))

        for row, product in enumerate(self.products):

            self.product_table.setItem(
                row,
                0,
                QTableWidgetItem(product.description)
            )

            self.product_table.setItem(
                row,
                1,
                QTableWidgetItem(product.status)
            )

            self.product_table.setItem(
                row,
                2,
                QTableWidgetItem(product.confidence)
            )

            self.product_table.setItem(
                row,
                3,
                QTableWidgetItem(product.engineden_url)
            )

    def select_excel(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Excel Workbook",
            "",
            "Excel Files (*.xlsx *.xls)"
        )

        if filename:
            self.excel_edit.setText(filename)

    def select_output(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Output Folder"
        )

        if folder:
            self.output_edit.setText(folder)