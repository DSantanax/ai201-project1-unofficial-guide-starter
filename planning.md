# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

OMSCS Georgia Tech Course Reviews & Structure for the Computing Systems specialization only.

This information is valuable because I only want information that can help me search the course catalog for reviews on specific courses based on my specialization. This will also be useful when I prompt if this course builds up to the next course or what should I take before this specific course. Multiple reviews have good information if a course is challenging and if its recommended to take it full time or part time while employed.

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|

| 1 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/artificial-intelligence/reviews>  |
| 2 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/data-and-visual-analytics/reviews>  |
| 3 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/high-performance-computing/reviews>  |
| 4 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/high-performance-computer-architecture/reviews>  |
| 5 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/human-computer-interaction/reviews> |
| 6 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/introduction-to-graduate-algorithms/reviews> |
| 7 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/computer-networks/reviews> |
| 8 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/introduction-to-information-security/reviews> |
| 9 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/software-development-process/reviews> |
| 10 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/software-architecture-and-design/reviews> |
| 11 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/advanced-operating-systems/reviews> |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
     Chunk size will start around 1000 characters.

**Overlap:**
     I will add an overlap of 50 characters.

**Reasoning:**
     This is due to some reviews being short compared to reviews that are very thorough. The overlap
     will add some buffer if needed. The Pros and Cons list are also compact compared to the written reviews.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
     all-MiniLM-L6-v2

**Top-k:**
     3

**Production tradeoff reflection:**
     Fixed size is a great choice for the model because the entire text document is for a specific course. All reviews are self-contained, however, they do vary
     from short and long reviews.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is the most time consuming course for the Computing Systems specialization? | |
| 2 | What 2 courses should not be taken together in the same semester because of the difficulty? | |
| 3 | What is a great first introductory course to take that is not too difficult or too easy? | |
| 4 | What is a great first introductory course to take that is easy? | |
| 5 | List the top 3 challenging courses | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Chunk sizing can cause issues due to the varying sizes of the reviews.

2. I provided the course catalog but I am not sure if it will distiguish what is core, elective, and not required for specialization.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

Document Ingesition (Txt files) -> Chunking (300 + 50 overlap) -> Vector store (ChromaDB) -> Retrieval (ChromaDB) -> Generation (all-MiniLM-L6-v2)

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
     Ill create a Claude project for Project 1 and give the format I have in the txt files for each course. Ill explain these are reviews and what the format already contains. I will also give a quick overwiew of the assignment. Ill ask Claude to implement a function called load_docs and chunk_docs based on my current plan. The load_docs will return a list of the filename, text, and the course name. This will be passed to the chunk_docs to create the chunks + overlap based on the text for each file which will return a list of chunks, filename, and unique ID.

**Milestone 4 — Embedding and retrieval:**
     Based on the previous input, I will ask Claude to embed and store this information into ChromaDB using the unique ID.
     For the retrieval section I will pass a query/question with k_results being the number of responses. This will use the collection to create a response that include the query, number of results to return, and the information to include which will be documents, metadata, and distances to prep for the generation.

**Milestone 5 — Generation and interface:**
     For the generation portion I ask Claude to use the model all-MiniLM-L6-v2 to create a grounded response by proving the # of reviews and the question in the user prompt. For the system prompt it must use what is given and avoid giving other information by stating they are not sure. The return will be the answer from the llm.

     For the UI, I will ask it to create a basic UI using Gradio that takes user input and uses the generation method to create a single response that will be displayed in the frontend.
