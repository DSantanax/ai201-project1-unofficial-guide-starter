"""Milestone 5 — Grounded generation over retrieved course reviews.

``generate`` retrieves the most relevant review chunks for a question and asks the LLM
to answer using only those reviews. It returns the answer string, so the Milestone 5 UI
can call it directly with the user's chat-box input.
"""

from groq import Groq

import config
from vectorstore import retrieve

SYSTEM_PROMPT = (
    "You are an assistant that answers questions about Georgia Tech OMSCS courses "
    "using ONLY the student reviews provided in the user's message. "
    "Do not use any outside knowledge or make up details. "
    "If the reviews do not contain enough information to answer, say you are not sure "
    "and restate the question rather than guessing."
)

# Reuse a single Groq client across calls.
_client = None


def _get_client() -> Groq:
    global _client
    if _client is None:
        _client = Groq(api_key=config.GROQ_API_KEY)
    return _client


def _format_reviews(results: dict) -> str:
    """Turn retrieved chunks into a numbered, source-attributed block for the prompt."""
    blocks = []
    for i, (doc, meta) in enumerate(
        zip(results["documents"], results["metadatas"]), start=1
    ):
        course = meta.get("course", "unknown course")
        blocks.append(f"Review {i} (course: {course}):\n{doc}")
    return "\n\n".join(blocks)


def generate(question: str, n_results: int = config.N_RESULTS) -> str:
    """Answer ``question`` grounded in the top ``n_results`` retrieved reviews.

    Returns the LLM's answer as a string for the UI to display.
    """
    results = retrieve(question, n_results=n_results)
    reviews = _format_reviews(results)

    user_prompt = (
        f"Here are {len(results['documents'])} student reviews to use:\n\n"
        f"{reviews}\n\n"
        f"Question: {question}"
    )

    response = _get_client().chat.completions.create(
        model=config.LLM_MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    question = "What is the most time consuming course?"
    answer = generate(question)
    print(answer)
