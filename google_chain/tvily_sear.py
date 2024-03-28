from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()
res = search.invoke("what is the panadol cf medicine used for")

print(res)