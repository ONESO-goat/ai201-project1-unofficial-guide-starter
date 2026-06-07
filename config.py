import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    EVENTBRITE_API_KEY = os.getenv("EVENTBRITE_API_KEY")
    LLM_MODEL = "llama-3.3-70b-versatile"
    CHUNK_SIZE = 300
    CHUNK_OVERLAP = 60
    MIN_CHUNK_LENGTH = 50

    # --- Embeddings ---
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    # --- Vector store ---
    CHROMA_COLLECTION = "unofficial_guide"
    CHROMA_PATH = "./chroma_db"

    # --- Retrieval ---
    N_RESULTS = 3

    # --- Documents ---
    DOCS_PATH = "./documents"
    
if not Config.GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY environment variable not found")

if __name__ == "__main__":
    print(Config.N_RESULTS)