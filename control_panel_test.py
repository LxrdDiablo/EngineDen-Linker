import sys

from PySide6.QtWidgets import QApplication

from gui.widgets.control_panel import ControlPanel


app = QApplication(sys.argv)

panel = ControlPanel()


panel.start_clicked.connect(
    lambda: print("Start")
)

panel.stop_clicked.connect(
    lambda: print("Stop")
)

panel.export_clicked.connect(
    lambda: print("Export")
)

panel.open_folder_clicked.connect(
    lambda: print("Open Folder")
)

panel.resize(700,100)

panel.show()

app.exec()