import re
from googlesearch.googlesearch import Search

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text


query = "panadol used for"
result = Search(query=query, language="en", number_of_results=10, retry_count=2,
                             parser="html.parser").as_dict()

results = result.get("results", [])

result_text = ""

for result in results:
    result_text += result.get("description") + "\n"

print(preprocess_text(result_text))
