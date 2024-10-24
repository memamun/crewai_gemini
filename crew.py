import os
from dotenv import load_dotenv
from litellm import completion
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# Load environment variables from .env file
load_dotenv()

# Get the API key from .env file
api_key = os.getenv("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = api_key

# Define the model
model_name = "gemini/gemini-1.5-flash"

# Define your agents with roles and goals
search_tool = DuckDuckGoSearchRun()

researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in AI and data science',
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends.
    You have a knack for dissecting complex data and presenting
    actionable insights.""",
    verbose=True,
    allow_delegation=True,
    memory=True,
    llm=model_name,  # using the model string
    tools=[search_tool]
)

writer = Agent(
    role='Tech Content Strategist',
    goal='Craft compelling content on AI tools',
    backstory="""You are a renowned Content Strategist, known for
    your insightful and engaging articles.
    You transform complex concepts into compelling narratives.""",
    verbose=True,
    allow_delegation=False,
    memory=True,
    llm=model_name,  # using the model string
    tools=[]
)

# Create tasks for your agents
task1 = Task(
    description="""Conduct a comprehensive analysis of the latest advancements in AI tools in 2024.
    Identify key trends, breakthrough technologies, and potential industry impacts.
    Your final answer MUST be a full analysis report""",
    agent=researcher,
    expected_output="Full analysis report on AI tools and best ai tools"
)

task2 = Task(
    description="""Using the insights provided, develop an engaging blog
    post that highlights the most significant AI advancements.
    Your post should be informative yet accessible, catering to a tech-savvy audience.
    Make it sound cool, avoid complex words so it doesn't sound like AI.
    Your final answer MUST be the full blog post of at least 5 paragraphs.""",
    agent=writer,
    expected_output="Blog post on AI tools and best ai tools"
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True
)

# Get your crew to work!
result = crew.kickoff()
print(result)
