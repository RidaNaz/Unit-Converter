from crewai import Agent, Task, Crew

# Define agents
conversion_agent = Agent(
    role="Unit Conversion Expert",
    goal="Accurately convert units",
    backstory="You are an expert in unit conversions and can handle any type of conversion."
)

validation_agent = Agent(
    role="Validation Expert",
    goal="Validate the accuracy of conversions",
    backstory="You ensure that all conversions are correct and reliable."
)

# Define tasks
conversion_task = Task(
    description=f"Convert {value} {from_unit} to {to_unit}",
    agent=conversion_agent
)

validation_task = Task(
    description=f"Validate the conversion of {value} {from_unit} to {to_unit}",
    agent=validation_agent
)

# Create crew
crew = Crew(
    agents=[conversion_agent, validation_agent],
    tasks=[conversion_task, validation_task]
)

# Execute crew
result = crew.kickoff()
st.success(f"CrewAI Result: {result}")