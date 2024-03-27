import re
from googlesearch.googlesearch import Search

query = "sanaullah bwithai"
result = Search(query=query, language="en", number_of_results=10, retry_count=2,
                             parser="html.parser").as_dict()

results = result.get("results", [])

result_text = ""

for result in results:
    print(result.get("description"))