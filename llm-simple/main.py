"""
main.py — chạy file này để test
"""
from llm import ask
import config

print(f"Using: {config.PROVIDER} / {config.OLLAMA_MODEL if config.PROVIDER == 'local' else 'claude-sonnet-4-6'}")
print("-" * 40)

# Test 1: câu hỏi đơn giản
answer = ask("Giải thích list comprehension trong Python bằng 2 câu ngắn")
print("Q: Giải thích list comprehension")
print(f"A: {answer}")
print()

# Test 2: tự thay câu hỏi của bạn
my_question = "Sự khác nhau giữa list và tuple trong Python là gì?"
answer2 = ask(my_question)
print(f"Q: {my_question}")
print(f"A: {answer2}")