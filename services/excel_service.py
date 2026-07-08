import pandas as pd

from models.product import Product


class ExcelService:

    def load_products(self, filename):

        df = pd.read_excel(filename)

        if "DESC" not in df.columns:
            raise Exception(
                "The workbook does not contain a 'DESC' column."
            )

        products = []

        for index, row in df.iterrows():

            description = str(row["DESC"]).strip()

            if description == "" or description.lower() == "nan":
                continue

            products.append(
                Product(
                    row_number=index + 2,
                    description=description,
                )
            )

        return products