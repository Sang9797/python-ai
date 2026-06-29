import os
from dotenv import load_dotenv
 
load_dotenv()
 
# Đổi dòng này để switch giữa local và cloud
PROVIDER = "local"   # "local" = Ollama | "cloud" = Claude
 
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:latest")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")