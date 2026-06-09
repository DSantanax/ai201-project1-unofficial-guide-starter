"""Milestone 4 — Embedding and retrieval with ChromaDB.

``embed_and_store`` encodes chunk texts with all-MiniLM-L6-v2 and persists them to a
ChromaDB collection. ``retrieve`` embeds a query and returns the top-k matching chunks.
Both are standalone functions; orchestration lives in main.py, and ``retrieve`` is
called by the Milestone 5 chat feature.
"""

import chromadb
from sentence_transformers import SentenceTransformer

import config

# Load the embedding model once and reuse it across calls.
_model = None


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(config.EMBEDDING_MODEL)
    return _model


def _get_collection():
    """Return the persistent ChromaDB collection, creating it if needed."""
    client = chromadb.PersistentClient(path=config.CHROMA_PATH)
    return client.get_or_create_collection(
        name=config.CHROMA_COLLECTION,
        # Cosine is what all-MiniLM-L6-v2 is trained for; makes distances
        # interpretable (0 = identical, 1 = unrelated). Baked in at creation time.
        metadata={"hnsw:space": "cosine"},
    )


def reset_collection() -> None:
    """Drop the collection so the index can be rebuilt cleanly (avoids duplicate ids)."""
    client = chromadb.PersistentClient(path=config.CHROMA_PATH)
    try:
        client.delete_collection(name=config.CHROMA_COLLECTION)
    except Exception:
        # Collection doesn't exist yet — nothing to delete.
        pass


def embed_and_store(chunks: list[dict]):
    """Embed each chunk's text and store it in ChromaDB keyed by its chunk_id.

    Stores ``documents`` (chunk text), ``metadatas`` (course title + source filename),
    and ``ids`` (unique chunk_id). Returns the populated collection.
    """
    texts = [c["chunk"] for c in chunks]
    ids = [c["chunk_id"] for c in chunks]
    metadatas = [{"course": c["course"], "filename": c["filename"]} for c in chunks]

    embeddings = _get_model().encode(
        texts, show_progress_bar=True, normalize_embeddings=True
    ).tolist()

    collection = _get_collection()
    collection.add(
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )
    return collection


def retrieve(query: str, n_results: int = config.N_RESULTS) -> dict:
    """Embed ``query`` and return the top ``n_results`` chunks from the collection.

    ChromaDB nests results one list per query; since we pass a single query we unwrap
    the first result, returning flat ``documents``/``metadatas``/``distances`` lists.
    """
    query_embedding = _get_model().encode(
        [query], normalize_embeddings=True
    ).tolist()

    response = _get_collection().query(
        query_embeddings=query_embedding,
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    return {
        "documents": response["documents"][0],
        "metadatas": response["metadatas"][0],
        "distances": response["distances"][0],
    }
