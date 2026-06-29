"""
llm.py — một function duy nhất: ask()
Dù dùng Ollama hay Claude, cách gọi đều giống nhau.
"""
import ollama
import anthropic
import config


def ask(message: str) -> str:
    """
    Gửi message tới LLM và nhận response dạng string.

    Ví dụ:
        answer = ask("Python là gì?")
        print(answer)
    """
    if config.PROVIDER == "local":
        return _ask_ollama(message)
    else:
        return _ask_claude(message)


def _ask_ollama(message: str) -> str:
    response = ollama.chat(
        model=config.OLLAMA_MODEL,
        messages=[{"role": "user", "content": message}],
    )
    return response["message"]["content"]


def _ask_claude(message: str) -> str:
    client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": message}],
    )
    return response.content[0].text