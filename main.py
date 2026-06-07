from AI import Chatbot
from sources import Sources
from emb import Embeddings
from gui import GUI

s = Sources()
e = Embeddings()
bot = Chatbot()
gui = GUI(bot, e)

def run_ingestion():
    """
    Load rule documents, chunk them, and store in ChromaDB.

    If the vector store is already populated, ingestion is skipped.
    To re-ingest (e.g. after changing your chunking strategy), delete the
    ./chroma_db folder and restart the app.
    """
    collection = e.get_collection()

    if collection.count() > 0:
        print(f"Vector store already populated ({collection.count()} chunks). Skipping ingestion.")
        print("To re-ingest, delete the ./chroma_db folder and restart.")
        return

    print("Ingesting rule documents...")
    data = s.sources(dict)
    all_chunks = []
    counter = 0
    if isinstance(data, dict):
        for source, dt in data.items():
            print(f"CURRENT SOURCE: {source}")
            
            for hackathon in dt:
                t = hackathon.get("themes", "tags")
                if not t:
                    t = "N/A"
                try:
                    chunks,counter = e.chunk_document(counter=counter,
                                            text=e.dict_to_string(hackathon),
                                            location=hackathon['location'],
                                            name=hackathon["name"], 
                                            start_date=hackathon.get("start_date", "N/A"),
                                            end_date=hackathon.get("end_date", "N/A"),
                                            price=hackathon.get("prize_amount", "N/A"),
                                            tags=t,
                                            source=hackathon["source"],
                                            is_free=hackathon.get('is_free', "N/A"),
                                            return_counter=True)
                    all_chunks.extend(chunks)
                except:
                    continue
                print(f"NEW RETURNED COUNTER: {counter}")
    print("Looping process completed")
    if all_chunks:
        e.embed_and_store(all_chunks)
        print(f"Ingestion complete. {len(all_chunks)} chunks stored.")
    else:
        print(
            "\n⚠️  No chunks produced. Make sure chunk_document() is implemented in ingest.py.\n"
            "    RulesBot will start, but won't be able to answer questions yet.\n"
        )


def main():
    """ This is a simple test to see if the chatbot can generate answers based on the provided chunks.
    We create a chatbot instance, an embeddings instance, and load the MLH breakdown document."""

    chunks = e.get_collection()
    if chunks.count() <= 0:
        run_ingestion()
        chunks = e.get_collection()
        
    print(f"Loaded {chunks.count()} chunks: [{chunks}]")
    #input("Press ENTER to continue...")
    questions = [ # my questions from planning.md
        "What are some upcoming hackathons?",
        "What are some free hackathons?",
        "I am visiting Californa, what is the hackthon history?",
        "What are some hackathons stated on reddit?",
        "What are the common themes for hackathons?",
        "Can you provide me hackathons that are online?",
        "What hackathon will you recommend?",
        "What hackathons will be taking place soon?",
    ]
    for q in questions:
        print(f"Question: {q}")
        print(f"Answer: {bot.generate(q, chunks=chunks)}")
        print("\n---\n")
        
if __name__ == "__main__":
    import traceback
    try:
        #run_ingestion()
        main()
        gui.demo.launch()
    except Exception as ex:
        print(f"ERROR: \n\t\u2022{ex}")
        traceback.print_exc()