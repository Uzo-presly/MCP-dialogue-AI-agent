# MCP Dialogue AI Agent

A simple Python demonstration of a tool-using AI agent built with
Ollama, LangGraph, and Model Context Protocol (MCP).

## What This Project Does

The application asks an AI agent to create a four-message dialogue
between Mary and a specified person.

The AI agent can discover and use tools exposed by an MCP server.

## Architecture

User
  ↓
client.py
  ↓
Ollama LLM
  ↓
LangGraph Agent
  ↓
MCP Client
  ↓
MCP Server
  ↓
Custom Tools

## MCP Tools

### yell()
Converts text to uppercase and adds exclamation marks.

### sarcasm()
Alternates character capitalization to create a simple sarcastic effect.

### polite_phrase()
Wraps a phrase in a polite response.

## Technologies

- Python
- Ollama
- LangChain
- LangGraph
- Model Context Protocol (MCP)

## Requirements

- Python 3
- Ollama
- llama3.2:1b
- Required Python packages

## Installation

Clone the repository:

git clone <YOUR-REPOSITORY-URL>

Enter the project:

cd my-mcp-agent-project

Create a virtual environment:

python3 -m venv .venv

Activate it:

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Install the Ollama Model

ollama pull llama3.2:1b

## Run

python3 client.py John

Replace John with another name.

## How It Works

1. client.py starts.
2. The MCP server is launched as a subprocess.
3. The MCP client connects to the server through stdio.
4. The client discovers the available MCP tools.
5. LangGraph provides the agent loop.
6. Ollama provides the language model.
7. The agent decides whether to use available tools.
8. The final dialogue is returned to the user.

## What I Learned

- How an LLM differs from an AI agent
- How an agent can use external tools
- How MCP exposes tools to an AI application
- How an MCP client communicates with an MCP server
- How local LLMs can be integrated into Python applications
- How LangGraph manages agent execution

## Future Improvements

- Add more useful tools
- Add a web-based interface
- Add persistent conversation memory
- Add logging and error handling
- Experiment with stronger local and cloud models
- Add automated tests