from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
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

        self.main_layout.addStretch()

    def build_header(self):

        title = QLabel("EngineDen Linker")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        subtitle = QLabel("Milestone 3 - Professional GUI")

        self.main_layout.addWidget(title)
        self.main_layout.addWidget(subtitle)

    def build_file_panel(self):

        excel_title = QLabel("Excel File")

        self.main_layout.addWidget(excel_title)

        excel_layout = QHBoxLayout()

        self.excel_edit = QLineEdit()
        self.excel_edit.setPlaceholderText("Select an Excel workbook...")

        excel_button = QPushButton("Browse")

        excel_button.clicked.connect(self.select_excel)

        excel_layout.addWidget(self.excel_edit)
        excel_layout.addWidget(excel_button)

        self.main_layout.addLayout(excel_layout)

        output_title = QLabel("Output Folder")

        self.main_layout.addWidget(output_title)

        output_layout = QHBoxLayout()

        self.output_edit = QLineEdit()
        self.output_edit.setPlaceholderText("Select output folder...")

        output_button = QPushButton("Browse")

        output_button.clicked.connect(self.select_output)

        output_layout.addWidget(self.output_edit)
        output_layout.addWidget(output_button)

        self.main_layout.addLayout(output_layout)

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