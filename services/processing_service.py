from models.product import Product
from services.engineden_service import EngineDenService
from services.logger_service import LoggerService


class ProcessingService:
    """
    Processes Product objects using EngineDenService.
    """

    def __init__(self):

        self.service = EngineDenService()
        self.logger = LoggerService()

    def process_product(self, product: Product) -> Product:

        self.logger.write(
            f"Searching: {product.description}"
        )

        result = self.service.search(
            product.description
        )

        product.processed = True

        if result.found:

            product.status = "Found"
            product.matched_name = result.matched_name
            product.engineden_url = result.product_url
            product.image_url = result.image_url
            product.confidence = result.confidence
            product.error = ""

            self.logger.write(
                f"FOUND ({result.confidence}%): {result.matched_name}"
            )

        else:

            product.status = "Not Found"
            product.error = result.error

            self.logger.write(
                f"NOT FOUND: {product.description}"
            )

        return product