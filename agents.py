from crewai import Agent
from crewai import LLM
from dotenv import load_dotenv
import os
from tools import tool
load_dotenv()

try:
    llm = LLM(
        model="groq/llama3-8b-8192",  
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
    )
except Exception as e:
    print(f"Error initializing LLM: {e}")

researcher_agent = Agent(
    role="Researcher",
    goal="Conduct comprehensive research on {company} and its industry position",
    verbose=True,
    memory=True,
    backstory="""
    You are a Researcher conducting detailed research on {company}.
    Your main role is to gather and analyze data related to the company's market position, products, technology infrastructure, and operational challenges.
    You will utilize reliable sources to provide comprehensive insights about {company}.
    """,
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

analyst_agent = Agent(
    role="Analyst",
    goal="Generate high-impact AI/ML use cases based on research findings",
    verbose=True,
    memory=True,
    backstory="""
    You are an Analyst evaluating the findings from the research on {company}.
    Your primary responsibility is to analyze the data and generate 5-8 detailed AI/ML use cases.
    You will focus on current industry adoption patterns, technical feasibility, expected ROI, and integration requirements.
    """,
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
