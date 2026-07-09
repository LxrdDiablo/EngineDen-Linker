from services.engineden_api import EngineDenAPI

api = EngineDenAPI()

results = api.search("Toyota 2KD Engine")

print()

print(f"Found {len(results)} result(s)\n")

for item in results:

    print(item["value"])
    print(item["url"])
    print(item["img"])
    print("-" * 60)