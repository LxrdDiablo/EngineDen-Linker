import sys

from PySide6.QtWidgets import QApplication

from gui.widgets.statistics_panel import StatisticsPanel

app = QApplication(sys.argv)

panel = StatisticsPanel()

panel.update_statistics({

    "total": 8314,

    "processed": 150,

    "found": 145,

    "missing": 5,

})

panel.show()

app.exec()