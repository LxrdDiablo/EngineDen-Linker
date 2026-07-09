from services.export_service import ExportService


class ExportController:

    def __init__(self):

        self.exporter = ExportService()

    def export(self, excel_file, output_folder, products):

        return self.exporter.export(
            excel_file,
            output_folder,
            products
        )