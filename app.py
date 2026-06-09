"""Milestone 5 — Gradio chat UI.

A simple front end: the user types a question, it's passed to ``generate`` (RAG over the
course reviews), and the single grounded answer is shown back.
"""

import gradio as gr

from generate import generate


def answer_question(question: str) -> str:
    if not question or not question.strip():
        return "Please enter a question about an OMSCS course."
    return generate(question)


demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(
        lines=2,
        label="Your question",
        placeholder="e.g. What is the most time-consuming course?",
    ),
    outputs=gr.Textbox(label="Answer", lines=10),
    title="OMSCS Unofficial Guide",
    description="Ask about Georgia Tech OMSCS courses. Answers are grounded in student reviews.",
)


if __name__ == "__main__":
    demo.launch()
