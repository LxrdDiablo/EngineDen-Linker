from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QPushButton,
)


class ControlPanel(QGroupBox):
    """
    Bottom control buttons.
    """

    start_clicked = Signal()
    stop_clicked = Signal()
    export_clicked = Signal()
    open_folder_clicked = Signal()

    def __init__(self):

        super().__init__("Controls")

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.start_button = QPushButton("▶ Start")
        self.stop_button = QPushButton("■ Stop")
        self.export_button = QPushButton("💾 Export Results")
        self.folder_button = QPushButton("📂 Open Output Folder")

        self.stop_button.setEnabled(False)
        self.export_button.setEnabled(False)

        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addStretch()
        layout.addWidget(self.export_button)
        layout.addWidget(self.folder_button)

        self.start_button.clicked.connect(
            self.start_clicked.emit
        )

        self.stop_button.clicked.connect(
            self.stop_clicked.emit
        )

        self.export_button.clicked.connect(
            self.export_clicked.emit
        )

        self.folder_button.clicked.connect(
            self.open_folder_clicked.emit
        )

    def processing_started(self):

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.export_button.setEnabled(False)

    def processing_finished(self):

        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.export_button.setEnabled(True)

    def processing_stopped(self):

        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)