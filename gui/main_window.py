from PySide6.QtCore import Qt, QThread
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QGroupBox,
    QGridLayout,
    QHeaderView,
)

from services.excel_service import ExcelService
from workers.processing_worker import ProcessingWorker


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.products = []

        self.thread = None
        self.worker = None

        self.setWindowTitle("EngineDen Linker v1.0")

        self.resize(1400, 850)

        self.setup_ui()
            def setup_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        self.main_layout = QVBoxLayout()

        central.setLayout(self.main_layout)

        self.build_header()

        self.build_file_panel()

        self.build_progress_panel()

        self.build_statistics_panel()

        self.build_product_table()

        self.build_control_panel()

def product_finished(self, product):

    for row, p in enumerate(self.products):

        if p.row_number == product.row_number:

            self.product_table.setItem(
                row,
                1,
                QTableWidgetItem(product.status)
            )

            self.product_table.setItem(
                row,
                2,
                QTableWidgetItem(str(product.confidence))
            )

            self.product_table.setItem(
                row,
                3,
                QTableWidgetItem(product.engineden_url)
            )

            break


def product_finished(self, product):

    for row, p in enumerate(self.products):

        if p.row_number != product.row_number:
            continue

        self.product_table.setItem(
            row,
            1,
            QTableWidgetItem(product.matched_name)
        )

        self.product_table.setItem(
            row,
            2,
            QTableWidgetItem(str(product.confidence))
        )

        self.product_table.setItem(
            row,
            3,
            QTableWidgetItem(product.status)
        )

        self.product_table.setItem(
            row,
            4,
            QTableWidgetItem(product.engineden_url)
        )

        break
        def build_header(self):

        title = QLabel("EngineDen Linker")

        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        subtitle = QLabel(
            "Automatic Engine Product Linking"
        )

        subtitle.setStyleSheet("""
            color:#aaaaaa;
            font-size:13px;
        """)

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
    
    def build_statistics_panel(self):

        group = QGroupBox("Statistics")

        layout = QGridLayout()

        group.setLayout(layout)

        self.total_label = QLabel("0")

        self.processed_label = QLabel("0")

        self.found_label = QLabel("0")

        self.missing_label = QLabel("0")

        self.accuracy_label = QLabel("0%")

        layout.addWidget(QLabel("Total"),0,0)
        layout.addWidget(self.total_label,0,1)

        layout.addWidget(QLabel("Processed"),1,0)
        layout.addWidget(self.processed_label,1,1)

        layout.addWidget(QLabel("Found"),2,0)
        layout.addWidget(self.found_label,2,1)

        layout.addWidget(QLabel("Missing"),3,0)
        layout.addWidget(self.missing_label,3,1)

        layout.addWidget(QLabel("Accuracy"),4,0)
        layout.addWidget(self.accuracy_label,4,1)

        self.main_layout.addWidget(group)
    
        def build_product_table(self):

        self.product_table = QTableWidget()

        self.product_table.setColumnCount(5)

        self.product_table.setHorizontalHeaderLabels([

            "Excel Product",

            "Matched Product",

            "Confidence",

            "Status",

            "EngineDen URL"

        ])

        header = self.product_table.horizontalHeader()

        header.setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )

        header.setSectionResizeMode(
            1,
            QHeaderView.Stretch
        )

        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeToContents
        )

        header.setSectionResizeMode(
            4,
            QHeaderView.Stretch
        )

        self.main_layout.addWidget(
            self.product_table
        )

    def build_control_panel(self):

        layout = QHBoxLayout()

        layout.addStretch()

        self.start_button = QPushButton("Start")
        self.stop_button.clicked.connect(
    self.stop_processing
)def stop_processing(self):

    if self.worker:

        self.worker.stop()

        self.status_label.setText(
            "Stopping..."
        )

        self.stop_button.setEnabled(False)

        self.start_button.clicked.connect(self.start_processing)
def start_processing(self):

    self.load_excel()

    if not self.products:
        return

    self.start_button.setEnabled(False)
    self.stop_button.setEnabled(True)

    self.progress_bar.setValue(0)

    self.thread = QThread()

    self.worker = ProcessingWorker(
        self.products
    )

    self.worker.moveToThread(self.thread)

    self.thread.started.connect(
        self.worker.run
    )

    self.worker.progress.connect(
        self.update_progress
    )

    self.worker.status.connect(
        self.update_status
    )

    self.worker.product_processed.connect(
        self.product_finished
    )

    self.worker.finished.connect(
        self.processing_finished
    )

    self.worker.finished.connect(
        self.thread.quit
    )

    self.thread.finished.connect(
        self.thread.deleteLater
    )

    self.thread.start()

    QMessageBox.information(
        self,
        "Next Step",
        f"{len(self.products)} products loaded.\n\n"
        "The processing worker will be connected next."
    )
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
            QTableWidgetItem("")
        )

        self.product_table.setItem(
            row,
            2,
            QTableWidgetItem("")
        )

        self.product_table.setItem(
            row,
            3,
            QTableWidgetItem("Waiting")
        )

        self.product_table.setItem(
            row,
            4,
            QTableWidgetItem("")
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