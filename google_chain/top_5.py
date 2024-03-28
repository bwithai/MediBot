import os
import pprint

from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool

os.environ["GOOGLE_CSE_ID"] = "7754a9fcd87a84485"
os.environ["GOOGLE_API_KEY"] = "AIzaSyD3Yhzxq5JJq6rxax60gRHDNDxUgWV7Wls"

search = GoogleSearchAPIWrapper()


def top5_results(query):
    return search.results(query, 5)


tool = Tool(
    name="Google Search Snippets",
    description="Search Google for recent results.",
    func=top5_results,
)

pprint.pprint(tool.run("panadol used for"))