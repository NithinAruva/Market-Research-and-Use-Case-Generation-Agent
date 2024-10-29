from crewai import Task
from tools import tool
from agents import researcher_agent, analyst_agent
from datetime import datetime
current_time = datetime.now().strftime("%H%M%S")

research_task = Task(
    description=(
        "Conduct comprehensive research on {company} and its industry position. Include:\n"
        "1. Industry segment analysis and market position\n"
        "2. Key products and manufacturing processes\n"
        "3. Current technology infrastructure\n"
        "4. Main operational challenges and opportunities\n\n"
        "Gather data from reliable sources and provide detailed findings."
    ),
    expected_output=(
        "Deliver a structured document containing:\n"
        "1. Industry analysis and market position summary\n"
        "2. Overview of key products and processes\n"
        "3. Technology infrastructure details\n"
        "4. Summary of operational challenges and opportunities\n\n"
        "Ensure that all findings are well-researched and sourced."
    ),
    tools=[tool],
    agent=researcher_agent,
)

use_case_prompt = """
Generate a detailed AI/ML use case analysis for {company} following this exact structure:

**GenAI & ML Use Cases for {company}**
[Company context and introduction paragraph about AI/ML opportunities]

**Use Case: [Use Case Name]**
* **Objective/Use Case**: [Clear statement of the problem being solved]
* **AI Application**: [Specific AI/ML technologies and implementation approach]
* **Cross-Functional Benefit**:
   * **[Department 1]**: [Specific benefit and impact]
   * **[Department 2]**: [Specific benefit and impact]
   * **[Department 3]**: [Specific benefit and impact]

Focus on these key areas:
1. Manufacturing process optimization
2. Quality control and assurance
3. Supply chain and inventory management
4. Predictive maintenance
5. Customer service enhancement

For each use case:
- Ensure clear business value proposition
- Include specific AI/ML technologies
- Identify cross-functional benefits
- Consider implementation feasibility
"""

analyst_task = Task(
    description=(
        f"Based on the research conducted for {{company}}, generate 3-5 high-impact AI/ML use cases.\n\n"
        f"Use this specific prompt for use case generation:\n{use_case_prompt}\n\n"
        "Analyze:\n"
        "1. Current industry AI/ML adoption patterns\n"
        "2. Technical feasibility of each use case\n"
        "3. Expected ROI and implementation complexity\n"
        "4. Integration requirements with existing systems"
    ),
    expected_output=(
        "Deliver a structured document containing:\n"
        "1. Company context and AI opportunity overview\n"
        "2. 5-8 detailed use cases following the exact format:\n"
        "   - Use case name and objective\n"
        "   - Specific AI application details\n"
        "   - Cross-functional benefits (3 departments minimum)\n"
        "3. Each use case should be practical and implementable\n\n"
        "Format the output exactly as shown in the example template."
    ),
    tools=[tool],
    agent=analyst_agent,
    output_file=f"report_{str(current_time)}.md"
)
