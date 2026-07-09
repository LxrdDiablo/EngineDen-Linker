from PySide6.QtCore import QObject, Signal

from services.processing_service import ProcessingService


class ProcessingWorker(QObject):
    """
    Background worker that processes products without
    freezing the GUI.
    """

    progress = Signal(int)
    status = Signal(str)
    product_processed = Signal(object)
    statistics = Signal(dict)
    finished = Signal()

    def __init__(self, products):

        super().__init__()

        self.products = products

        self.processor = ProcessingService()

        self.running = True

    def stop(self):

        self.running = False

    def run(self):

        total = len(self.products)

        found = 0
        missing = 0

        for index, product in enumerate(self.products):

            if not self.running:
                break

            self.status.emit(
                f"Searching: {product.description}"
            )

            product = self.processor.process_product(product)

            if product.status == "Found":
                found += 1
            else:
                missing += 1

            self.product_processed.emit(product)

            self.progress.emit(
                int(((index + 1) / total) * 100)
            )

            self.statistics.emit({

                "processed": index + 1,

                "found": found,

                "missing": missing,

                "total": total

            })

        self.finished.emit()