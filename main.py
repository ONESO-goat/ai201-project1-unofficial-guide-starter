from AI import Chatbot
from sources import MLH_breakdown
from emb import Embeddings

if __name__ == "__main__":
    bot = Chatbot()
    e = Embeddings()
    docs = MLH_breakdown()
    chunks = e.chunk_document(e.dict_to_string(docs))
    questions = [
        "What are some upcoming hackathons?",
        "What are some free hackathons?",
        "Who are the winners from Bitcamp 2025?",
        "I want to focus on Data science, which tech event is best to gain the knowledge?",
        "What hackathons will be taking place near Cambridge, MA?",
    ]
    for q in questions:
        print(f"Question: {q}")
        print(f"Answer: {bot.generate(q, chunks=chunks)}")
        print("\n---\n")
