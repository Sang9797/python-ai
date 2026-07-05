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
# from tokenization import get_tokenizer, tokenize_text, encode_tokens, decode_tokens
# text = "Java is awesome"
# tokens = tokenize_text(text)
# print(f"Tokens: {tokens}")
# ids = encode_tokens(tokens)
# print(f"Encoded IDs: {ids}")
# decoded_text = decode_tokens(ids)
# print(f"Decoded text: {decoded_text}")

# Embedding
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode("I love AI")
print(len(embeddings))

# Compare similarity
from sklearn.metrics.pairwise import cosine_similarity
# Example (real models have 384, 768, or 1024 dimensions):
# Token            Embedding

# [CLS]      [0.2, 0.5, 0.1]
# I          [0.3, 0.8, 0.2]
# love       [0.9, 0.1, 0.4]
# AI         [0.8, 0.3, 0.9]
# [SEP]      [0.4, 0.6, 0.2]
# Mean pooling simply computes the average of every dimension.

# Example:
# Token vectors

# [1,2,3]
# [4,5,6]
# [7,8,9]

# Mean pooling computes

# Dimension 1
# (1+4+7)/3 = 4

# Dimension 2
# (2+5+8)/3 = 5

# Dimension 3
# (3+6+9)/3 = 6

# Result
# [4,5,6]

# That's the sentence embedding
emb1 = model.encode("dog") 
emb2 = model.encode("puppy")
# print(f"Embedding 1: {emb1}")
# print(f"Embedding 2: {emb2}")
similarity = cosine_similarity([emb1], [emb2])
print(f"Similarity: {similarity[0][0]}")