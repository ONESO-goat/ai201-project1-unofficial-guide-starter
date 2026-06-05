import os
import chromadb
from chromadb.utils import embedding_functions
from config import Config






class Embeddings:
    def __init__(self, embedding_model=Config.LLM_MODEL, n_results=Config.N_RESULTS):
        self.embedding_model = embedding_model
        self.n_results = n_results
        self._ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=Config.EMBEDDING_MODEL
        )
        self._client = chromadb.PersistentClient(path=Config.CHROMA_PATH)
        self._collection = self._client.get_or_create_collection(
            name=Config.CHROMA_COLLECTION,
            embedding_function=self._ef,
            metadata={"hnsw:space": "cosine"},
        )

    # def load_documents(self, docs_path=Config.DOCS_PATH):
    #     """Load all .txt rule documents from the docs folder."""
    #     documents = []
    #     for filename in sorted(os.listdir(docs_path)):
    #         if filename.endswith(".txt"):
    #             filepath = os.path.join(docs_path, filename)
    #             with open(filepath, "r", encoding="utf-8") as f:
    #                 text = f.read()
    #             game_name = filename.replace(".txt", "").replace("_", " ").title()
    #             documents.append({
    #                 "game": game_name,
    #                 "filename": filename,
    #                 "text": text,
    #             })
    #     print(f"Loaded {len(documents)} rule document(s): {[d['game'] for d in documents]}")
    #     return documents


    def chunk_document(self, text, info):
        
        chunk_size = Config.CHUNK_SIZE
        overlap = Config.CHUNK_OVERLAP
        min_length = Config.MIN_CHUNK_LENGTH

        chunks = []
        prefix = info.lower().replace(" ", "_")
        counter = 0

        start = 0
        while start < len(text): # start loop
            end = start + chunk_size # define end of chunk
            chunk_text = text[start:end].strip() # start to end, trim whitespace

            if len(chunk_text) >= min_length:
                # if the length of the chunk is long enough, add it to the list with metadata
                chunks.append({
                    "text": chunk_text,
                    "subject": info,
                    "chunk_id": f"{prefix}_{counter}",
                })
                counter += 1 # increase counter for unique chunk_id

            # Advance by (chunk_size - overlap) so the next chunk shares
            # `overlap` characters with the tail of this one.
            start += chunk_size - overlap # move the start point forward by chunk_size minus the overlap to create the next chunk

        return chunks
