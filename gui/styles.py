"""
Application style sheet.
"""

DARK_STYLE = """
QMainWindow {
    background-color: #202124;
}

QWidget {
    background-color: #202124;
    color: white;
    font-size: 10pt;
}

QLabel {
    color: white;
}

QLineEdit {
    background-color: #2b2b2b;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 6px;
}

QPushButton {
    background-color: #0078D7;
    color: white;
    border-radius: 4px;
    padding: 8px;
}

QPushButton:hover {
    background-color: #1A88E5;
}

QPushButton:disabled {
    background-color: #555;
}

QProgressBar {
    border: 1px solid #444;
    border-radius: 4px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #00AA55;
}

QTableWidget {
    background-color: #2b2b2b;
    alternate-background-color: #323232;
    gridline-color: #555;
}

QHeaderView::section {
    background-color: #3a3a3a;
    color: white;
    padding: 5px;
}

QTextEdit {
    background-color: #2b2b2b;
}
"""