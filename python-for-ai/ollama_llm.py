# from langchain_core.tools import tool
# from langchain_ollama import ChatOllama

# @tool
# def calculate_total(price: float, quantity: int) -> float:
#     """Calculate total price."""
#     return price * quantity

# llm = ChatOllama(
#     model="gemma4:latest",
#     temperature=0
# )

# llm_with_tools = llm.bind_tools([calculate_total])

# response = llm_with_tools.invoke(
#     "A book costs 2.5 dollars. I buy 8 books. What is the total?"
# )

# print("content:", response.content)
# print("tool_calls:", response.tool_calls)

# for tool_call in response.tool_calls:
#     if tool_call["name"] == "calculate_total":
#         result = calculate_total.invoke(tool_call["args"])
#         print("tool result:", result)

# LangGraph Example

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

@tool
def calculate_total(price: float, quantity: int) -> float:
    """Calculate total price."""
    return price * quantity

model = ChatOllama(
    model="llama3.2:latest",
    temperature=0,
)

agent = create_agent(
    model=model,
    tools=[calculate_total],
    system_prompt="You are a helpful shopping assistant."
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "A book costs 2.5 dollars. I buy 8 books. What is the total?"
            }
        ]
    }
)

print(result["messages"][-1].content)

# OpenAI Agents SDK

# from agents import Agent, Runner, function_tool

# @function_tool
# def calculate_total(price: float, quantity: int) -> float:
#     """Calculate total price."""
#     return price * quantity

# agent = Agent( 
#     name="Shopping Agent", 
#     instructions="Use tools when calculation is needed.", 
#     tools=[calculate_total] 
# )

# result = Runner.run_sync(
#     agent,
#     "A notebook costs 2.5 dollars. I buy 8. What is the total?"
# )

# print(result.final_output)