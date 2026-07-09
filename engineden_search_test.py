from services.engineden_service import EngineDenService

service = EngineDenService()

result = service.search("Toyota 2KD Engine")

print()

print("FOUND")
print(result.found)

print()

print("MATCH")
print(result.matched_name)

print()

print("CONFIDENCE")
print(result.confidence)

print()

print("URL")
print(result.product_url)

print()

print("IMAGE")
print(result.image_url)