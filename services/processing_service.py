from models.product import Product
from services.engineden_service import EngineDenService


class ProcessingService:
    """
    Processes a Product by searching EngineDen and
    copying the search results back into the Product.
    """

    def __init__(self):

        self.service = EngineDenService()

    def process_product(self, product: Product) -> Product:

        result = self.service.search(product.description)

        product.processed = True

        if result.found:

            product.status = "Found"

            product.matched_name = result.matched_name

            product.engineden_url = result.product_url

            product.image_url = result.image_url

            product.confidence = result.confidence

            product.error = ""

        else:

            product.status = "Not Found"

            product.error = result.error

        return product