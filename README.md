# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain


"Hackthons for students", this can include free - paid - beginner - AI produced - etc.

---

## Document Sources


| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | reddit/hackthons |place to find hackthons | |
| 2 | reddit/tech  | place to find tech related events| |
| 3 | reddit/cs | place to find cs related events| |
| 4 | reddit/networking | place to find networking related events| |
| 5 | google/hackathons | place to find hackthons | |
| 6 | your-univerity/college-website/tech | place to find tech related events | |
| 7 | your-univerity/clubs | place to find clubs inside your school| |
| 8 | your-city/local event | place to find local events | |
| 9 | ChatGpt/prompt="Hackathons best for students" | AI search 
| 10 | | | |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 300

**Overlap:** 1

**Why these choices fit your documents:** Simple queries

**Final chunk count:** 50-300

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** State the main key from my curosity ex:
What are **free** **long term** **hackthons** that are coming this coming **year** in **<my area>** 

**How source attribution is surfaced in the response:** 

---

## Evaluation Report

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | "What are some upcoming hackathons near me?" |  "list of hackathons near me" |
| 2 | "What are some free hackathons near me?" | "list of free hackthons" |

| 3 | "Who are the winners from the '<hackathon name>' hackathon?" | "Name or Names of winners" |
| 4 | "I want to focus on <field>, which tech event is best to gain the knowledge?"| "List of events that related to that spific field" |
| 5 | "What hackathons will be taking place in <state>? | "List of hackathons inside that state" |

**Retrieval quality:** **Relevant** / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
