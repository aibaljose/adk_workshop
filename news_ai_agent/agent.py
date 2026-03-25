# from google.adk.agents import Agent
# from google.adk.tools import google_search
# from .util import load_instructions

# # Define the News Agent with a supported model
# news_agent = Agent(
#     name="MalayalamNewsAgent",
#     model="gemini-2.5-flash", # <--- UPDATE THIS LINE
#     description="An agent that searches and summarizes latest news.",
#     instruction=load_instructions(),
#     tools=[google_search]
# )

# root_agent = news_agent







from google.adk.agents import Agent
from google.adk.tools import google_search, AgentTool
from .tool import send_actual_email
from .util import load_instructions

# 1. THE RESEARCHER (Encapsulated)
search_agent = Agent(
    name="SearchSpecialist",
    model="gemini-2.5-flash",
    description="An expert researcher that finds current news using Google Search.",
    instruction="Search for the latest 3 facts on the topic. Return only the facts.",
    tools=[google_search]
)

# Convert the agent into a tool the Manager can use
search_tool = AgentTool(search_agent)

# 2. THE MANAGER (The Root Agent)
news_manager = Agent(
    name="NewsManager",
    model="gemini-2.5-flash",
    description="Manager that coordinates news searching and emailing.",
    # We load the instructions from the text file here:
    instruction=load_instructions("instructions.txt"), 
    tools=[search_tool, send_actual_email]
)

root_agent = news_manager