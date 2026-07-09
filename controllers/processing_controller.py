from PySide6.QtCore import QThread

from workers.processing_worker import ProcessingWorker


class ProcessingController:
    """
    Coordinates the processing workflow between
    the GUI and the backend services.
    """

    def __init__(self, window):

        self.window = window

        self.thread = None
        self.worker = None

    def start(self, products):

        self.thread = QThread()

        self.worker = ProcessingWorker(products)

        self.worker.moveToThread(self.thread)

        # Thread starts worker
        self.thread.started.connect(
            self.worker.run
        )

        # GUI Updates
        self.worker.progress.connect(
            self.window.progress_panel.set_progress
        )

        self.worker.status.connect(
            self.window.progress_panel.set_status
        )

        self.worker.statistics.connect(
            self.window.statistics_panel.update_statistics
        )

        self.worker.product_processed.connect(
            self.window.results_table.update_product
        )

        self.worker.finished.connect(
            self.window.processing_finished
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()

    def stop(self):

        if self.worker:

            self.worker.stop()