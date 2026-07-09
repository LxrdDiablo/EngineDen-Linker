from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFileDialog,
    QGridLayout,
    QGroupBox,
    QLineEdit,
    QPushButton,
)


class FilePanel(QGroupBox):
    """
    Handles Excel file and output folder selection.
    """

    excel_changed = Signal(str)
    output_changed = Signal(str)

    def __init__(self):

        super().__init__("Project")

        layout = QGridLayout()
        self.setLayout(layout)

        self.excel_edit = QLineEdit()
        self.output_edit = QLineEdit()

        excel_button = QPushButton("Browse")
        output_button = QPushButton("Browse")

        excel_button.clicked.connect(
            self.select_excel
        )

        output_button.clicked.connect(
            self.select_output
        )

        layout.addWidget(self.excel_edit, 0, 0)
        layout.addWidget(excel_button, 0, 1)

        layout.addWidget(self.output_edit, 1, 0)
        layout.addWidget(output_button, 1, 1)

    def select_excel(self):

        filename, _ = QFileDialog.getOpenFileName(

            self,

            "Select Excel Workbook",

            "",

            "Excel Files (*.xlsx *.xls)"

        )

        if filename:

            self.excel_edit.setText(filename)

            self.excel_changed.emit(filename)

    def select_output(self):

        folder = QFileDialog.getExistingDirectory(

            self,

            "Select Output Folder"

        )

        if folder:

            self.output_edit.setText(folder)

            self.output_changed.emit(folder)

    def excel_file(self):

        return self.excel_edit.text()

    def output_folder(self):

        return self.output_edit.text()