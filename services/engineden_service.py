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

        print("\n" + "=" * 70)
        print("SEARCHING:", product_name)
        print("=" * 70)

        # -----------------------------------
        # Search EngineDen AJAX API
        # -----------------------------------

        suggestions = self.api.search(product_name)

        print("\nSuggestions returned:")
        print(suggestions)

        if not suggestions:

            print("No suggestions returned.")

            result.error = "No products found."

            return result

        # -----------------------------------
        # Find best match
        # -----------------------------------

        best, score = self.matcher.find_best(
            product_name,
            suggestions
        )

        print("\nBest match:")
        print(best)
        print("Score:", score)

        if best is None:

            result.error = "No suitable match."

            return result

        # -----------------------------------
        # Validate URL
        # -----------------------------------

        url = best.get("url", "")

        print("\nURL:")
        print(url)

        if not url:

            print("ERROR: URL is empty!")

            result.error = "Matched product has no URL."

            return result

        # -----------------------------------
        # Download full-size image
        # -----------------------------------

        image = self.parser.get_full_image(url)

        print("\nImage:")
        print(image)

        # -----------------------------------
        # Build SearchResult
        # -----------------------------------

        result.found = True
        result.product_name = product_name
        result.matched_name = best.get("value", "")
        result.product_url = url
        result.image_url = image
        result.confidence = score

        print("\nSearch completed successfully.")

        return result