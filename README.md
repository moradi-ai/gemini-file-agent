# Gemini File Agent

An autonomous file management agent built with Python, Google GenAI SDK, and `gemini-3.5-flash-lite`.

The agent uses **Automatic Function Calling (AFC)** via chat sessions to inspect local directories, read files, and generate concise summaries autonomously.

## Project Structure

- `smart_agent.py`: Core agent loop handling user chat and function execution.
- `tools.py`: Local workspace tools (`list_workspace_files`, `read_workspace_file`, `write_summary_file`).
- `config.example.py`: Configuration template for API keys and model parameters.

## Setup & Running

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/moradi-ai/gemini-file-agent.git](https://github.com/moradi-ai/gemini-file-agent.git)
   cd gemini-file-agent
