import asyncio
import sys


from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client




# Initialize the local Ollama language model.
# The model runs locally on this computer rather than using a cloud API.
model = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)

# Configure the exact background shell path to spawn your server.py file
server_params = StdioServerParameters(
    command=sys.executable,   # Use the SAME Python environment
    args=["server.py"],
)

def get_prompt(name):
    return f"Create a dialogue between Mary and {name}. There should be 4 messages in total. {name} should yell every time and Mary should be very polite."

async def run_agent(name_string):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_agent(model, tools)

            prompt = get_prompt(name_string)
            agent_response = await agent.ainvoke({"messages": prompt})

            # Print the final result directly onto your Ubuntu terminal window screen!
            print("\n" + "="*40)
            print("         SUCCESSFUL AGENT OUTPUT        ")
            print("="*40)
            print(agent_response["messages"][-1].content)
            print("="*40 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 client.py <name>")
        sys.exit(1)

    # Grab the clean string argument passed via the terminal prompt
    target_name = sys.argv[1]
    asyncio.run(run_agent(target_name))
