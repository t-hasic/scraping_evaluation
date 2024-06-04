import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

graph_config = {
   "llm": {
      "api_key": openai_key,
      "model": "gpt-3.5-turbo",
   },
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
   prompt="Please provide the name, price, and listing URL for each of the items on the page.",
   # also accepts a string with the already downloaded HTML code
   source="https://scrapeme.live/shop/",
   config=graph_config
)

result = smart_scraper_graph.run()
print(result)
