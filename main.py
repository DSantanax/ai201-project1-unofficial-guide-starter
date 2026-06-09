"""Pipeline entry point: build the ChromaDB index from the course documents.

Loads the documents, splits them into fixed-size chunks, and embeds + stores them.
Retrieval is exposed by vectorstore.retrieve and is exercised by the Milestone 5 chat
feature rather than here.
"""

from ingestion import chunk_documents, load_docs
from vectorstore import embed_and_store, reset_collection


def build_index():
    docs = load_docs()
    chunks = chunk_documents(docs)
    print(f"loaded {len(docs)} docs -> {len(chunks)} chunks")

    reset_collection()
    collection = embed_and_store(chunks)
    print(f"stored {collection.count()} chunks in the '{collection.name}' collection")


if __name__ == "__main__":
    build_index()
