# Gemini File Agent

An autonomous file management agent built with Python, Google GenAI SDK, and gemini-3.5-flash-lite.

The agent uses **Automatic Function Calling (AFC)** via chat sessions to inspect local directories, read files, and generate concise summaries autonomously.

## Project Structure

- smart_agent.py: Core agent loop handling user chat and function execution.
- 	ools.py: Local workspace tools (list_workspace_files, 
ead_workspace_file, write_summary_file).
- config.example.py: Configuration template for API keys and model parameters.

## Setup & Running

1. **Clone the repository:**
   `ash
   git clone [https://github.com/moradi-ai/gemini-file-agent.git](https://github.com/moradi-ai/gemini-file-agent.git)
   cd gemini-file-agent
   `

2. **Install dependencies:**
   `ash
   pip install google-genai
   `

3. **Configure API Key:**
   - Copy config.example.py to config.py.
   - Add your Gemini API key inside config.py.

4. **Launch the agent:**
   `ash
   python smart_agent.py
   `
