from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Server")


@mcp.tool()
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate final price after discount."""
    return price * (1 - discount_percent / 100)


@mcp.tool()
def calculate_total(price: float, quantity: int) -> float:
    """Calculate total price."""
    return price * quantity


if __name__ == "__main__":
    mcp.run(transport="stdio")