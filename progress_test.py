import sys

from PySide6.QtWidgets import QApplication

from gui.widgets.progress_panel import ProgressPanel

app = QApplication(sys.argv)

panel = ProgressPanel()

panel.set_progress(65)

panel.set_status(
    "Searching Toyota 2KD Engine..."
)

panel.resize(500,120)

panel.show()

app.exec()