# Import the FastMCP class from the Anthropic MCP SDK to build an MCP tool server
from mcp.server.fastmcp import FastMCP

# Create a server instance named "Dialogue" so clients can identify it
mcp = FastMCP("Dialogue")

@mcp.tool()
def yell(phrase: str) -> str:
    """Turns a phrase into a loud shout as if the person is yelling."""
    # Converts text string to uppercase and appends exclamation marks
    return phrase.upper() + "!!!"

@mcp.tool()
def sarcasm(phrase: str) -> str:
    """Turns a phrase into a sarcastic remark."""
    sarcastic_phrase = ""
    # Loop through every character and alternate casing based on positional indexes
    for i, char in enumerate(phrase):
        if i % 2 == 0:
            sarcastic_phrase += char.upper()
        else:
            sarcastic_phrase += char.lower()
    return sarcastic_phrase + " ~"

@mcp.tool()
def polite_phrase(phrase: str) -> str:
    """Refines a sentence to make it exceptionally polite, formal, and courteous for Mary."""
    # Formats a polite greeting template around the text string
    return f"Dearest friend, if I may humbly say: {phrase} I wish you a wonderful day ahead."

if __name__ == "__main__":
    # Start the server using Standard Input/Output (stdio) for local communication
    mcp.run(transport="stdio")
