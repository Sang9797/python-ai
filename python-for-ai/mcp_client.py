import asyncio

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mcp_server.py"],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()

    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0,
    )

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful math assistant."
    )

    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "A product costs 100 dollars with 15% discount. What is the final price?"
                }
            ]
        }
    )

    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())