import pandas as pd


class ExcelReader:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        df = pd.read_excel(self.filename)

        if "DESC" not in df.columns:
            raise Exception("DESC column not found.")

        return df
