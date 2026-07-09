import re


class QueryBuilder:

    def build(self, description):

        description = description.strip()

        queries = []

        # Original description
        queries.append(description)

        words = description.split()

        # Engine code
        code = None

        for word in words:
            if re.match(r"^[0-9A-Za-z]{2,6}$", word):
                if any(c.isdigit() for c in word):
                    code = word.upper()
                    break

        if code:

            queries.append(code)

            queries.append(f"{code} Engine")

            brand = words[0]

            queries.append(f"{brand} {code}")

        # Remove duplicates while preserving order
        unique = []

        for q in queries:
            if q not in unique:
                unique.append(q)

        return unique