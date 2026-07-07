from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QProgressBar,
    QVBoxLayout,
    QHBoxLayout,
)
from PySide6.QtWidgets import QMessageBox

from gui.log_widget import LogWidget
from excel.reader import ExcelReader

class MainWindow(QMainWindow):
    def start_processing(self):

    filename = self.excel_path.text()

    if filename == "":
        QMessageBox.warning(
            self,
            "No File",
            "Please select an Excel file."
        )
        return

    try:

        self.status.setText("Loading spreadsheet...")

        self.log_window.log("Loading Excel...")

        reader = ExcelReader(filename)

        df = reader.load()

        rows = len(df)

        self.log_window.log(f"{rows} products loaded.")

        self.progress.setValue(100)

        self.status.setText("Spreadsheet Loaded Successfully")

    except Exception as e:

        QMessageBox.critical(
            self,
            "Error",
            str(e)
        )

        self.log_window.log(str(e))

    def __init__(self):
        super().__init__()

        self.setWindowTitle("EngineDen Linker v1.0")
        self.resize(900, 600)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        title = QLabel("EngineDen Linker")
        title.setStyleSheet("font-size:26px;font-weight:bold;")
        layout.addWidget(title)

        # -----------------------
        # Excel File
        # -----------------------

        excel_layout = QHBoxLayout()

        self.excel_path = QLineEdit()
        self.excel_path.setPlaceholderText("Select Excel File...")

        browse_excel = QPushButton("Browse")

        browse_excel.clicked.connect(self.select_excel)

        excel_layout.addWidget(self.excel_path)
        excel_layout.addWidget(browse_excel)

        layout.addWidget(QLabel("Excel File"))
        layout.addLayout(excel_layout)

        # -----------------------
        # Output Folder
        # -----------------------

        output_layout = QHBoxLayout()

        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Select Output Folder...")

        browse_output = QPushButton("Browse")

        browse_output.clicked.connect(self.select_output)

        output_layout.addWidget(self.output_path)
        output_layout.addWidget(browse_output)

        layout.addWidget(QLabel("Output Folder"))
        layout.addLayout(output_layout)

        # -----------------------
        # Progress
        # -----------------------

        layout.addWidget(QLabel("Progress"))

        self.progress = QProgressBar()

        self.progress.setValue(0)

        layout.addWidget(self.progress)

        # -----------------------
        # Status
        # -----------------------
layout.addWidget(QLabel("Log"))

self.log_window = LogWidget()

layout.addWidget(self.log_window)
        self.status = QLabel("Waiting...")

        layout.addWidget(self.status)

        # -----------------------
        # Buttons
        # -----------------------

        buttons = QHBoxLayout()

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_processing)

        self.stop_button = QPushButton("Stop")

        self.stop_button.setEnabled(False)

        buttons.addStretch()

        buttons.addWidget(self.start_button)

        buttons.addWidget(self.stop_button)

        layout.addLayout(buttons)

    def select_excel(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Excel File",
            "",
            "Excel Files (*.xlsx *.xls)"
        )

        if filename:
            self.excel_path.setText(filename)

    def select_output(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Output Folder"
        )

        if folder:
            self.output_path.setText(folder)