from crewai import Crew
from agents import property_researcher
from tasks import property_research_task

crew=Crew(
    agents=[property_researcher],
    tasks=[property_research_task],
    verbose=True
)

task_output=crew.kickoff()
print(task_output)  