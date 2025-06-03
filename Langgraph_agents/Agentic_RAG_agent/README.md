# Agentic RAG Agent

A modular, agentic Retrieval-Augmented Generation (RAG) system built with LangGraph and LangChain, featuring tool integration and Hugging Face LLM support.

## Overview
This project demonstrates an agentic RAG pipeline that leverages a graph-based workflow to answer user queries using a combination of retrieval, search, weather, and model statistics tools. It is designed for extensibility and easy integration of new tools.

## Features
- **Agentic RAG**: Uses a graph-based agent to orchestrate tool use and LLM responses.
- **Hugging Face LLM**: Integrates with Hugging Face's Qwen2.5-Coder-32B-Instruct model.
- **Tool Integration**:
  - Guest info retrieval (BM25-based)
  - DuckDuckGo web search
  - Dummy weather information
  - Hugging Face Hub model statistics
- **Extensible**: Easily add new tools or modify the agent's workflow.

## Installation
1. **Clone the repository** and navigate to the project folder:
   ```sh
   cd Langgraph_agents/Agentic_RAG_agent
   ```
2. **Set up a virtual environment** (recommended):
   ```sh
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Unix/Mac:
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   # or, if using uv:
   uv pip install -r requirements.txt
   ```
   Or use the provided `pyproject.toml` with your preferred tool (e.g., `uv`, `pip`, or `poetry`).

4. **Set environment variables**:
   - Create a `.env` or `env.local` file with your Hugging Face API token:
     ```env
     HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
     ```

## Usage
Run the main agent script:
```sh
uv run main.py
# or
python main.py
```

Example output:
```
Hello from agentic-rag-agent!
🎩 Alfred's Response:
<agent's answer here>
```

## Project Structure
```
Langgraph_agents/Agentic_RAG_agent/
├── main.py              # Entry point, agent and graph definition
├── data.py              # Loads and formats guest dataset
├── tools/
│   ├── retriever.py     # Guest info retrieval tool (BM25)
│   ├── hub_stat_tool.py # Hugging Face Hub stats tool
│   ├── search_tool.py   # DuckDuckGo search tool
│   └── tools.py         # Weather info tool
├── pyproject.toml       # Project dependencies
├── env.local            # Environment variables (not committed)
└── README.md            # Project documentation
```