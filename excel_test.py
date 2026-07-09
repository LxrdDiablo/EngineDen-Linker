from services.excel_service import ExcelService

service = ExcelService()

products = service.load_products("products.xlsx")

print()

print(f"Loaded {len(products)} products")

print()

print(products[0])