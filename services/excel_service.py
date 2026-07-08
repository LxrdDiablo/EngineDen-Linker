import pandas as pd

from models.product import Product


class ExcelService:

    def load_products(self, filename):

        df = pd.read_excel(filename)

        if "DESC" not in df.columns:
            raise Exception(
                "Column 'DESC' was not found in the Excel file."
            )

        products = []

        for index, row in df.iterrows():

            description = str(row["DESC"]).strip()

            if description == "" or description.lower() == "nan":
                continue

            product = Product(
                row_number=index + 2,
                description=description
            )

            products.append(product)

        return products