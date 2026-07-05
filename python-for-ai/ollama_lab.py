# import ollama

# response = ollama.chat(
#     model="llama3.2:latest",
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain what an AI agent is in simple words."
#         }
#     ]
# )

# print(response["message"]["content"])

# Add memory
# memory = []

# def chat_with_memory(user_message: str): 
#     memory.append(
#         {
#             "role": "user",
#             "content": user_message
#         })
#     response = ollama.chat(
#         model="llama3.2:latest",
#         messages=memory
#     )

#     assistant_message = response["message"]["content"]
#     memory.append(
#         {
#             "role": "assistant",
#             "content": assistant_message
#         }
#     )
#     return assistant_message

# print(chat_with_memory("My favorite programming language is Java.")) 
# print(chat_with_memory("What is my favorite programming language?"))

# Tool calling manually
import ollama

def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_total",
            "description": "Calculate total price. Always use this tool for price * quantity questions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "price": {"type": "number"},
                    "quantity": {"type": "integer"}
                },
                "required": ["price", "quantity"]
            }
        }
    }
]

messages = [
    {
        "role": "system",
        "content": "You must use the calculate_total tool when calculating total price."
    },
    {
        "role": "user",
        "content": "A notebook costs 2.5 dollars. I buy 8 notebooks. What is the total?"
    }
]

response = ollama.chat(
    model="llama3.2:latest",
    messages=messages,
    tools=tools
)

message = response["message"]
messages.append(message)

print("Assistant message:", message)

if message.get("tool_calls"):
    for tool_call in message["tool_calls"]:
        name = tool_call["function"]["name"]
        args = tool_call["function"]["arguments"]

        if name == "calculate_total":
            args = tool_call["function"]["arguments"]

            result = calculate_total(
                price=float(args["price"]),
                quantity=int(args["quantity"])
            )
            messages.append({
                "role": "tool",
                "tool_name": name,
                "content": str(result)
            })

    final_response = ollama.chat(
        model="llama3.2:latest",
        messages=messages,
        tools=tools
    )

    print(final_response["message"]["content"])
else:
    print("No tool call. Model answered directly:")
    print(message["content"])

