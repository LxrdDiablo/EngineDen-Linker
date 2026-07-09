from models.product import Product
from services.processing_service import ProcessingService

processor = ProcessingService()

product = Product(
    row_number=1,
    description="Toyota 2KD Engine"
)

product = processor.process_product(product)

print()

print("Description")
print(product.description)

print()

print("Matched")
print(product.matched_name)

print()

print("Confidence")
print(product.confidence)

print()

print("Status")
print(product.status)

print()

print("URL")
print(product.engineden_url)

print()

print("Image")
print(product.image_url)

print()

print("Processed")
print(product.processed)

print()

print("Error")
print(product.error)