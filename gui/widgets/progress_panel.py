from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QProgressBar,
    QVBoxLayout,
)


class ProgressPanel(QGroupBox):
    """
    Displays processing progress and current status.
    """

    def __init__(self):

        super().__init__("Progress")

        layout = QVBoxLayout()

        self.setLayout(layout)

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.status = QLabel("Waiting...")
        self.status.setWordWrap(True)

        layout.addWidget(self.progress)
        layout.addWidget(self.status)

    def set_progress(self, value):

        self.progress.setValue(value)
        self.progress.setTextVisible(True)
        
    def set_status(self, text):

        self.status.setText(text)

    def reset(self):

        self.progress.setValue(0)
        self.status.setText("Waiting...")