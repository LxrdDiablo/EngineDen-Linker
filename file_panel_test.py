import sys

from PySide6.QtWidgets import QApplication

from gui.widgets.file_panel import FilePanel


def excel(path):

    print("Excel:", path)


def output(path):

    print("Output:", path)


app = QApplication(sys.argv)

panel = FilePanel()

panel.excel_changed.connect(excel)

panel.output_changed.connect(output)

panel.resize(700,120)

panel.show()

app.exec()