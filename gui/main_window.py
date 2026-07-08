from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EngineDen Linker v1.0")
        self.resize(1100, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        title = QLabel("EngineDen Linker")
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
        """)

        subtitle = QLabel("Milestone 3 - Professional GUI")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addStretch()