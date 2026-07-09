from services.engineden_service import EngineDenService

service = EngineDenService()

result = service.search(
    "Toyota 2KD Engine"
)

print()

print("Found:", result.found)

print()

print("Matched:")

print(result.matched_name)

print()

print("Confidence:")

print(result.confidence)

print()

print("URL:")

print(result.product_url)

print()

print("Image:")

print(result.image_url)