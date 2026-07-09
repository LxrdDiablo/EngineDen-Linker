import os
from datetime import datetime

from openpyxl import load_workbook


class ExportService:
    """
    Exports processed products to a new Excel workbook.
    """

    def export(self, input_file, output_folder, products):

        workbook = load_workbook(input_file)
        sheet = workbook.active

        columns = {
            "Matched Product": 6,
            "Confidence": 7,
            "EngineDen URL": 8,
            "Image URL": 9,
            "Status": 10,
        }

        for title, col in columns.items():
            sheet.cell(row=1, column=col).value = title

        for product in products:

            row = product.row_number

            sheet.cell(row=row, column=6).value = product.matched_name
            sheet.cell(row=row, column=7).value = product.confidence
            sheet.cell(row=row, column=8).value = product.engineden_url
            sheet.cell(row=row, column=9).value = product.image_url
            sheet.cell(row=row, column=10).value = product.status

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"EngineDen_Output_{timestamp}.xlsx"

        output_path = os.path.join(
            output_folder,
            filename
        )

        workbook.save(output_path)
        workbook.close()

        return output_path