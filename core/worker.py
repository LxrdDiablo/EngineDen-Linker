from PySide6.QtCore import QObject, Signal


class Worker(QObject):

    progress = Signal(int)

    status = Signal(str)

    finished = Signal()

    error = Signal(str)