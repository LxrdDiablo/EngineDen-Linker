from PySide6.QtCore import QThread
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QMessageBox,
)

from gui.widgets.file_panel import FilePanel
from gui.widgets.progress_panel import ProgressPanel
from gui.widgets.statistics_panel import StatisticsPanel
from gui.widgets.results_table import ResultsTable
from gui.widgets.control_panel import ControlPanel

from services.excel_service import ExcelService
from services.export_service import ExportService

from workers.processing_worker import ProcessingWorker


class MainWindow(QMainWindow):
    """
    Main application window.
    Coordinates the GUI and background processing.
    """

    def __init__(self):

        super().__init__()

        self.products = []

        self.thread = None
        self.worker = None

        self.excel_service = ExcelService()
        self.export_service = ExportService()

        self.setWindowTitle("EngineDen Linker v1.0")

        self.resize(1400, 850)

        self.build_ui()

        self.connect_signals()

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        central.setLayout(layout)

        self.file_panel = FilePanel()

        self.progress_panel = ProgressPanel()

        self.statistics_panel = StatisticsPanel()

        self.results_table = ResultsTable()

        self.control_panel = ControlPanel()

        layout.addWidget(self.file_panel)
        layout.addWidget(self.progress_panel)
        layout.addWidget(self.statistics_panel)
        layout.addWidget(self.results_table)
        layout.addWidget(self.control_panel)

    def connect_signals(self):

        self.control_panel.start_clicked.connect(
            self.start_processing
        )

        self.control_panel.stop_clicked.connect(
            self.stop_processing
        )

        self.control_panel.export_clicked.connect(
            self.export_results
        )

        self.control_panel.open_folder_clicked.connect(
            self.open_output_folder
        )

    def start_processing(self):

        excel = self.file_panel.excel_file()

        if not excel:

            QMessageBox.warning(
                self,
                "No Excel File",
                "Please select an Excel workbook."
            )

            return

        try:

            self.products = self.excel_service.load_products(excel)

if self.file_panel.is_test_mode():

    self.products = self.products[
        :self.file_panel.row_limit()
    ]
        except Exception as e:

            QMessageBox.critical(
                self,
                "Excel Error",
                str(e)
            )

            return

        self.results_table.load_products(
            self.products
        )

        self.statistics_panel.update_statistics({

            "total": len(self.products),

            "processed": 0,

            "found": 0,

            "missing": 0

        })

        self.progress_panel.reset()

        self.control_panel.processing_started()

        self.thread = QThread()

        self.worker = ProcessingWorker(
            self.products
        )

        self.worker.moveToThread(
            self.thread
        )

        self.thread.started.connect(
            self.worker.run
        )

        self.worker.progress.connect(
            self.progress_panel.set_progress
        )

        self.worker.status.connect(
            self.progress_panel.set_status
        )

        self.worker.statistics.connect(
            self.statistics_panel.update_statistics
        )

        self.worker.product_processed.connect(
            self.results_table.update_product
        )

        self.worker.finished.connect(
            self.processing_finished
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()

    def stop_processing(self):

        if self.worker:

            self.worker.stop()

    def processing_finished(self):

    self.control_panel.processing_finished()

    self.progress_panel.set_status(
        "Processing Complete"
    )

    try:

        from services.export_service import ExportService

        exporter = ExportService()

        output_file = exporter.export(
            self.file_panel.excel_file(),
            self.file_panel.output_folder(),
            self.products
        )

        QMessageBox.information(
            self,
            "Complete",
            f"Processing finished.\n\n"
            f"Results saved to:\n\n{output_file}"
        )

    except Exception as e:

        QMessageBox.critical(
            self,
            "Export Error",
            str(e)
        )