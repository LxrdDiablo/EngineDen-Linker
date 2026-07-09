from models.search_result import SearchResult

from services.engineden_api import EngineDenAPI
from services.matcher_service import MatcherService
from services.product_page_parser import ProductPageParser


class EngineDenService:
    """
    Coordinates the complete EngineDen lookup process.
    """

    def __init__(self):

        self.api = EngineDenAPI()
        self.matcher = MatcherService()
        self.parser = ProductPageParser()

    def search(self, product_name):

        result = SearchResult()

        suggestions = self.api.search(product_name)

        if not suggestions:

            result.error = "No products found."

            return result

        best, score = self.matcher.find_best(
            product_name,
            suggestions
        )

        if best is None:

            result.error = "No suitable match."

            return result

        image = self.parser.get_full_image(
            best["url"]
        )

        result.found = True

        result.product_name = product_name

        result.matched_name = best["value"]

        result.product_url = best["url"]

        result.image_url = image

        result.confidence = score

        return result