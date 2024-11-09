# Market Research and Use-Case Generation Agent

This Multi-Agent generates relevant AI and Generative AI (GenAI) use cases for a given Company or Industry. The system will conduct market research, understand the industry and product, and provide resource assets for AI/ML solutions, focusing on enhancing operations and customer experiences.

## Features

- **Automated Market Research**: Utilizes Agents to search, analyze, and extract valuable insights from a variety of sources.
- **Use Case Generation**: Based on market data, the agent generates practical use cases and provide resource assets for AI/ML Solutions.
- **Streamlit Integration**: Provides an easy-to-use interface for managing and visualizing results.

# WorkFlow
![Screenshot 2024-11-09 184710](https://github.com/user-attachments/assets/b2f34475-e6ee-4309-8928-dbf822944a84)

## Methodology

The project was structured into several key components, which include the development of a Streamlit application, the configuration of AI agents for research and analysis, and the integration of necessary tools for data retrieval and processing.

### 1. Streamlit Application
- A user-friendly interface was created using Streamlit, allowing users to input a company name.
- A custom class, `StreamToContainer`, was developed to capture and display system output in real-time, providing feedback and displaying reference links within the Streamlit UI.

### 2. AI Agents
- Two AI agents were defined using the CrewAI library:
  - **Researcher Agent**: Conducts comprehensive research on the selected company and its industry, with a focus on market position, product offerings, technology infrastructure, and operational challenges.
  - **Analyst Agent**: Generates high-impact AI/ML use cases based on the research findings, considering industry trends, technical feasibility, expected ROI, and integration requirements.
- The agents utilize the Groq LLM, configured with an API key stored in environment variables, to process natural language data and extract insights.

### 3. Task Definitions
- The research and analysis processes were carefully structured to guide the agents:
  - **Research Task**: Provides detailed instructions for conducting a market analysis and generating a structured report with relevant findings.
  - **Analyst Task**: Uses a specific prompt to produce actionable AI/ML use cases based on the research, emphasizing the business value and feasibility of each case.

### 4. Tool Integration
- **TavilySearchResults** (from LangChain community): This tool was integrated to allow the agents to retrieve reliable information from various sources, enriching the research process and ensuring accuracy.

### 5. Execution Flow
- Once a company name is submitted, the Streamlit application initiates the research process with the Researcher Agent, followed by the Analyst Agent’s evaluation to generate relevant use cases.


## Technologies Used

- **Python**: Core programming language for backend logic.
- **Streamlit**: Provides the web-based UI for user input and result display.
- **CrewAI**: Used to configure and execute the AI agents.
- **LangChain**: Framework for facilitate the integration of large language models.
- **Groq API**:  Facilitates the integration of large language models.
- **TavilySearchResults**: Provides real-time, accurate, and unbiased information, enabling AI applications to retrieve and process data efficiently.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NithinAruva/Market-Research-and-Use-Case-Generation-Agent.git
   cd Market-Research-and-Use-Case-Generation-Agent
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add API keys in .env:
   ```bash
   GROQ_API_KEY=""
   TAVILY_API_KEY=""
   ```

## Usage

**Run the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for feature enhancements, bug fixes, or documentation improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
