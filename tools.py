from langchain_community.tools import TavilySearchResults
import os
api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    raise ValueError("TAVILY_API_KEY is not set.")

tool = TavilySearchResults(api_key=api_key)

