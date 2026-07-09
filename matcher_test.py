from services.engineden_api import EngineDenAPI
from services.matcher_service import MatcherService

api = EngineDenAPI()
matcher = MatcherService()

results = api.search("Toyota 2KD Engine")

best, score = matcher.find_best(
    "Toyota 2KD Engine",
    results
)

print()

print(best["value"])

print()

print(score)