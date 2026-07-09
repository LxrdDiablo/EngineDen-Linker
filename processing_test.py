from models.product import Product
from services.processing_service import ProcessingService

processor = ProcessingService()

product = Product(
    row_number=1,
    description="Toyota 2KD Engine"
)

product = processor.process_product(product)

print()
print("Description :", product.description)
print("Matched     :", product.matched_name)
print("Confidence  :", product.confidence)
print("Status      :", product.status)
print("URL         :", product.engineden_url)
print("Image       :", product.image_url)
print("Error       :", product.error)