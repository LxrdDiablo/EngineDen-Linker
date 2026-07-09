from PySide6.QtWidgets import (
    QLabel,
    QGridLayout,
    QGroupBox,
)


class StatisticsPanel(QGroupBox):
    """
    Displays processing statistics.
    """

    def __init__(self):

        super().__init__("Statistics")

        layout = QGridLayout()
        self.setLayout(layout)

        self.total = QLabel("0")
        self.processed = QLabel("0")
        self.found = QLabel("0")
        self.missing = QLabel("0")
        self.accuracy = QLabel("0.0%")

        labels = [
            ("Total", self.total),
            ("Processed", self.processed),
            ("Found", self.found),
            ("Missing", self.missing),
            ("Accuracy", self.accuracy),
        ]

        for row, (title, value) in enumerate(labels):
            layout.addWidget(QLabel(title), row, 0)
            layout.addWidget(value, row, 1)

    def update_statistics(self, stats):

        total = stats.get("total", 0)
        processed = stats.get("processed", 0)
        found = stats.get("found", 0)
        missing = stats.get("missing", 0)

        self.total.setText(str(total))
        self.processed.setText(str(processed))
        self.found.setText(str(found))
        self.missing.setText(str(missing))

        if processed > 0:
            accuracy = (found / processed) * 100
        else:
            accuracy = 0

        self.accuracy.setText(f"{accuracy:.1f}%")

    def reset(self):

        self.update_statistics({
            "total": 0,
            "processed": 0,
            "found": 0,
            "missing": 0,
        })