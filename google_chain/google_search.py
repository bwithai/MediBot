import os
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool

os.environ["GOOGLE_CSE_ID"] = "7754a9fcd87a84485"
os.environ["GOOGLE_API_KEY"] = "AIzaSyD3Yhzxq5JJq6rxax60gRHDNDxUgWV7Wls"

search = GoogleSearchAPIWrapper()

tool = Tool(
    name="google_search",
    description="Search Google for recent results.",
    func=search.run,
)

print(tool.run("panadol used for"))