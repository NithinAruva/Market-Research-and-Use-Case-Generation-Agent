import streamlit as st
import re
import sys
from crewai import Crew, Process
from agents import researcher_agent, analyst_agent
from tasks import research_task, analyst_task

# Used to stream sys output on the Streamlit frontend
class StreamToContainer:
    def __init__(self, container):
        self.container = container
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']  
        self.color_index = 0  

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        # Apply coloring based on task and agent names in the output
        if "Entering new CrewAgentExecutor chain" in cleaned_data:
            self.color_index = (self.color_index + 1) % len(self.colors)
            cleaned_data = cleaned_data.replace("Entering new CrewAgentExecutor chain", f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]")

        if "Researcher" in cleaned_data:
            cleaned_data = cleaned_data.replace("Researcher", f":{self.colors[self.color_index]}[Researcher]")
        if "Analyst" in cleaned_data:
            cleaned_data = cleaned_data.replace("Analyst", f":{self.colors[self.color_index]}[Analyst]")
        if "Finished chain." in cleaned_data:
            cleaned_data = cleaned_data.replace("Finished chain.", f":{self.colors[self.color_index]}[Finished chain.]")

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.container.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []

# Streamlit app UI
st.header("Market Research and Use Case Generation Agent")

with st.form("form"):
    company = st.text_input("Enter the name of the Company", key="company")
    submitted = st.form_submit_button("Submit")

if submitted:
    with st.spinner("🤖 **Agents at work...**"):
        with st.container():
            sys.stdout = StreamToContainer(st)  # Redirect stdout to display in Streamlit

            # Define the Crew with agents and tasks
            crew = Crew(
                agents=[researcher_agent, analyst_agent],
                tasks=[research_task, analyst_task],
                process=Process.sequential,
                verbose=True
            )

            # Execute the Crew process and get the result
            result = crew.kickoff(inputs={"company": company})

        st.success("✅ Your Report is ready!") 
    st.subheader("GenAI Use Cases")
    st.markdown(result)
