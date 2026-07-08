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
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

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

        excel_layout = QHBoxLayout()

        self.excel_edit = QLineEdit()
        self.excel_edit.setPlaceholderText("Select an Excel workbook...")

        excel_button = QPushButton("Browse")
        excel_button.clicked.connect(self.select_excel)

        excel_layout.addWidget(self.excel_edit)
        excel_layout.addWidget(excel_button)

        self.main_layout.addLayout(excel_layout)

        self.main_layout.addWidget(QLabel("Output Folder"))

        output_layout = QHBoxLayout()

        self.output_edit = QLineEdit()
        self.output_edit.setPlaceholderText("Select output folder...")

        output_button = QPushButton("Browse")
        output_button.clicked.connect(self.select_output)

        output_layout.addWidget(self.output_edit)
        output_layout.addWidget(output_button)

        self.main_layout.addLayout(output_layout)

    def build_progress_panel(self):

        self.main_layout.addWidget(QLabel("Progress"))

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
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
            "EngineDen URL"
        ])

        self.main_layout.addWidget(self.product_table)

    def build_control_panel(self):

        button_layout = QHBoxLayout()

        button_layout.addStretch()

        self.start_button = QPushButton("Start")

        self.stop_button = QPushButton("Stop")
        self.stop_button.setEnabled(False)

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)

        self.main_layout.addLayout(button_layout)

    def select_excel(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Excel File",
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