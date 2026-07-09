import re

from rapidfuzz import fuzz


class MatcherService:
    """
    Intelligent matcher for EngineDen products.
    """

    def normalize(self, text):

        text = text.lower()

        text = re.sub(r"\([^)]*\)", "", text)

        text = re.sub(r"[^a-z0-9 ]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def extract_engine_code(self, text):

        words = self.normalize(text).split()

        for word in words:

            if any(c.isdigit() for c in word):

                return word.upper()

        return ""

    def find_best(self, search_text, suggestions):

        if not suggestions:
            return None, 0

        search_clean = self.normalize(search_text)

        search_code = self.extract_engine_code(search_text)

        best = None
        best_score = -1

        for suggestion in suggestions:

            title = suggestion["value"]

            title_clean = self.normalize(title)

            score = fuzz.token_sort_ratio(
                search_clean,
                title_clean
            )

            title_code = self.extract_engine_code(title)

            if (
                search_code
                and search_code == title_code
            ):
                score += 50

            score = min(100, int(score))

            if score > best_score:

                best_score = score
                best = suggestion

        return best, best_score