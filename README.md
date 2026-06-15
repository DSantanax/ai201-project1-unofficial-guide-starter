# The Unofficial Guide — Project 1

---

## Domain

OMSCS Georgia Tech Course Reviews & Structure for the Computing Systems specialization only.

This information is valuable because I only want information that can help me search the course catalog for reviews on specific courses based on my specialization. This will also be useful on suggestions when taking a course such as the next course or what should I take before this specific course. Reviews have good information if a course is challenging and if its recommended to take it full time or part time while employed.

---

## Document Sources

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/artificial-intelligence/reviews> |
| 2 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/data-and-visual-analytics/reviews> |
| 3 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/high-performance-computing/reviews> |
| 4 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/high-performance-computer-architecture/reviews> |
| 5 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/human-computer-interaction/reviews> |
| 6 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/introduction-to-graduate-algorithms/reviews> |
| 7 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/computer-networks/reviews> |
| 8 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/introduction-to-information-security/reviews> |
| 9 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/software-development-process/reviews> |
| 10 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/software-architecture-and-design/reviews> |
| 11 | omscentral | Course offered in the program | <https://www.omscentral.com/courses/advanced-operating-systems/reviews> |

---

## Chunking Strategy

**Chunk size:**
     Chunk size will start around 1000 characters. That is because reviews from the OMSCentral are extensive and provide good information.

**Overlap:**
     I will add an overlap of 100 characters since some reviews may extend over the chunk size.

**Why these choices fit your documents:**
     This is due to some reviews being short compared to reviews that are very thorough. The overlap
     will add some buffer if needed. The Pros and Cons list are also compact compared to the written reviews. I did some prepocessing because I had to create the format from scrapping the data off the websites. This also includes removing any format I used.

**Final chunk count:**
     800 characters

---

## Embedding Model

**Model used:**
     sentence-transformers (all-MiniLM-L6-v2)

**Top-k:**
     3

**Production tradeoff reflection:**

     Fixed size is a great choice for the model because the entire text document is for a specific course. All reviews are self-contained, however, they do vary from short and long reviews. 
     However, OMSCS is global and having multilingual support would be benificial. This would also take into consideration expenses because it will be used quite often and will require API restrictions such as the throttling.
---

## Grounded Generation

**System prompt grounding instruction:**
     "You are an assistant that answers questions about Georgia Tech OMSCS courses "
     "using ONLY the student reviews provided in the message. Please include the source and cite the reviews."
     "Do not use any outside knowledge or make up details. "
     "If the reviews do not contain enough information to answer, say you are not sure "
     "and ask the user to restate the question rather than guessing."

**How source attribution is surfaced in the response:**
     The source quotes specific reviews and includes the course number/name.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What is the most time consuming that required mainly reading and not applying programming concepts? | CS6750 Human Computer Interaction | Based on the provided reviews, it appears that the course CS6750 Human Computer Interaction required a significant amount of reading and writing, with a lot of material and concepts to learn, digest, understand, and apply (Review 4). The student mentioned that they had to read several academic papers and write reports weekly, and that they wrote 11 papers for the course. They also mentioned that they spent a significant amount of time watching videos, reading papers, and performing peer reviews. | Relevant | Accurate |
| 2 | What 2 courses should not be taken together in the same semester because of the difficulty? | AI / GA / HPC / or HPCA | Based on the reviews provided, I am not sure which two courses should not be taken together in the same semester because of the difficulty. The reviews mention that certain courses are challenging, such as Introduction to Graduate Algorithms (Review 4) and Artificial Intelligence (Review 2), but they do not explicitly state which courses should not be taken together. | Relevant | Partially Accurate |
| 3 | What is a great first introductory course to take that is not too difficult or too easy? | Computer Networks or Software Development Process | Based on the student reviews provided, it seems that CSE6242 Data and Visual Analytics might be a good introductory course. Review 4 describes it as "an intro to ML/Data Science" and states that "The class wasn't difficult, but it was challenging." This suggests that the course may be a good starting point for those new to the field. However, Review 2 warns that the course is very easy, calling it a "cake course" where you can "coast with minimal effort." | Partially relevant. | Partially accurate |
| 4 | What is a great first introductory course to take that is easy? | Based on the data CSE 6242 is an easy course. | According to Review 2 (course: CSE6242 Data and Visual Analytics), the course CSE6242 is described as a "cake" course, where you can "coast with minimal effort" and it's rated as 1/5 in terms of difficulty. The reviewer mentions that it's a good course to take if you want to spend the least amount of effort and learn very little, making it a potentially easy introductory course. (Source: Review 2, Georgia Tech Student) | Relevant | Partially accurate |
| 5 | List the top 3 challenging courses | GA / AI / HPC | Based on the provided student reviews, I can see that the course "Introduction to Graduate Algorithms" (CS6515) is considered one of the most difficult courses. However, I am not sure about the top 3 challenging courses as the reviews only mention this specific course. One review (Review 184) mentions that "Introduction to Graduate Algorithms" is "one of the most difficult courses in the masters" for the student, but it does not provide a ranking or comparison with other courses. | Partially relevant | Inaccurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

**Question that failed:**
     List the top 3 challenging courses

**What the system returned:**
     Based on the provided student reviews, I can see that the course "Introduction to Graduate Algorithms" (CS6515) is considered one of the most difficult courses. However, I am not sure about the top 3 challenging courses as the reviews only mention this specific course.

**Root cause (tied to a specific pipeline stage):**
     This is possibly tied to data gathering and limited course information because I provided 11 courses with hundreds of reviews each. It did return some courses but not what I expected.

**What you would change to fix it:**
     I would list the entire course catalog and a list of courses available per specialization. This would be helpful to make comparison and list courses relevant to the specialization I am interested in.
     The format I used to parse likely needed tuning as well because I included other information that was not needed. I likely need to also update the prompt since it may be too broad but the data needs more tuning.

---

## Spec Reflection

**One way the spec helped you during implementation:**
     The spec sheet helped me understand the overall architecture and layout of the project. It gave a brief overview and allowed me to prepare each section before coding.
     This also assisted me with AI generated responses because the spec sheet was reviewed and it helped the Claude understand my question in depth.

**One way your implementation diverged from the spec, and why:**
     I had to change the fixed size, k-length, and adjust my questions with Claude. I updated my code and my spec after each milestone. Also, I had split my sections per file similar to our Lab 1 project 
     and change my discussion to include code organization.

---

## AI Usage->

**Instance 1**:

Prompt: Based on my MIlestone 3 I plan on creating a RAG model. that uses a fixed size method based on chunking.  I already created the txt files for 11 courses with review, rating, difficulty, and other information. My load_docs function will return a list objects containing the filename, the text within that file, and the course name which is the file name. It will have a list of objects for each file. This input will then be passed into the chunk_documents that will take the file text and the name of the course to create a chunking of 350 characters with an overlap of 50 characters until its finished reading the entire text of the file. This method will return a list of objects containing the chunks, course name, and a unique chunk id. I will then pass these chunks into the ChromaDB to embed it but thats for my next milestone.

Outcome: It tried to modify my files immediately after reading my spec and question. Also, the outcome was all in a single file rather than taking into consideration the future milestones and splitting the work into different files/folders which I could have specified. I had to override the execution method to convert it into a plan instead where I can modify the changes.

**Instance 2**:

Prompt: Now that Milestone 3 is complete, I plan on passing the chunking object list into the Embedding function process to save this information to ChromaDB with the unique chunk_id. This function will add the embeded list and store the chunks using the collection from chromaDB with document (chunk text), metadatas (title), and ids (chunk_id) as parameters.

The retreive function will have the query and number of results to retrieve the response which will contain the format document, metadatas, and distance. The return will the first result of the response list.

Outcome: Claude reorganized my code and created 2 functions from the spec list based on my prompt. It also moved my main function as I specified this to keep my code clean. One thing it did do that I later planned on changing was the reset collection for chroma db because it was reset on every run. I also had to stop Claude due to issues it was getting when trying to test the changes by running commands and not receiving the response it needed from my virtual environment. This was likely due to permission issues and issues with Claude not seeing my .venv enabled.
