from PySide6.QtWidgets import (
    QFileDialog,
    QGridLayout,
    QGroupBox,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QLabel,
    QSpinBox,
)


class FilePanel(QGroupBox):
    """
    Handles Excel file and output folder selection.
    """

    excel_changed = Signal(str)
    output_changed = Signal(str)

    def __init__(self):

        super().__init__("Project")

        self.test_mode = QCheckBox("Test Mode")

self.limit = QSpinBox()

self.limit.setMinimum(1)
self.limit.setMaximum(10000)
self.limit.setValue(100)

layout.addWidget(self.test_mode, 2, 0)

layout.addWidget(QLabel("Rows"), 2, 1)

layout.addWidget(self.limit, 2, 2)

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

        def is_test_mode(self):

    return self.test_mode.isChecked()


def row_limit(self):

    return self.limit.value()