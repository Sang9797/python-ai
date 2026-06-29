def greet(name:str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))

numbers = [ 1, 2, 3, 4, 5]

for num in numbers:
    print(f"Number: {num}")

user = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(user["name"])

result = [x**2 for x in numbers]

# Lambda
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print("Sorted users by age:")
for user in sorted(users, key=lambda x: x["age"]):
    print(f"{user['name']} - {user['age']}")

# Tokenization
from tokenization import get_tokenizer, tokenize_text, encode_tokens, decode_tokens
text = "Hello, how are you?"
tokens = tokenize_text(text)
print(f"Tokens: {tokens}")
ids = encode_tokens(tokens)
print(f"Encoded IDs: {ids}")
decoded_text = decode_tokens(tokens)
print(f"Decoded text: {decoded_text}")