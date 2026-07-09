from services.query_builder import QueryBuilder

builder = QueryBuilder()

queries = builder.build("Toyota 2KD Engine")

for q in queries:
    print(q)