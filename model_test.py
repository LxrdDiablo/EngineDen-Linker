from models.product import Product
from models.search_result import SearchResult

p = Product(
    row_number=1,
    description="Toyota 2KD Engine"
)

r = SearchResult()

print(p)
print()
print(r)