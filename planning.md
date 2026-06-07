# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

"hackthons or tech related events students can attend"
---

## Documents
reddit/hackthons 
reddit/tech 
reddit/cs 
reddit/networking 
google/hackathons
your-uni-website/tech
your-uni/clubs
<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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
| 10 | MLH.io | place filled with hackathons| |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 70


**Overlap:** 1

**Reasoning:** simple text on the information on the hackathon

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | "What are some upcoming hackathons?" |  "list of hackathons" |
| 2 | "What are some free hackathons?" | "list of free hackthons" |

| 3 | "Can you the winners from <hackathon name>?" | "Name or Names of previous winners" |
| 4 | "I want to focus on <field>, which tech event is best to gain the knowledge?"| "List of events that related to that spific field" |
| 5 | "What hackathons will be taking place near <address>? | "List of hackathons" |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Events that arent related to my topic

2. Not enough information on the provided response, E.Q the date it's taking place.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

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


**Milestone 4 — Embedding and retrieval:**
Question: What are some upcoming hackathons?
Answer: Based on the provided results, here are some upcoming hackathons:

1. GDG Solution Hacks - June 27-29, Toronto, Canada
2. SpurHacks - June 20-22, Waterloo, Ontario, Canada
3. Hack4Bengal 4.0 - June 20-22, Newtown, West Bengal, India
4. Hack 4 Her - June 14-15, Monterrey, Nuevo León, Mexico
5. Global Hack Week: GenAI - June 13-19, Everywhere, Worldwide
6. MasseyHacks - May 17-18, Windsor, Ontario, Canada
7. JAMHacks 9 - May 16-18, Waterloo, Ontario, Canada
8. NMIT HACKS 2025 - May 16-18, Bengaluru, Karnataka, India
9. DesignVerse at UCR - May 10-11, Riverside, California, US
10. HACKMESA - May 9-10, Los Angeles, CA, US
11. Global Hack Week: Open Source Week - May 9-15, Everywhere, Worldwide
12. GDSCHACKS - May 2-4, Guelph, Ontario, Canada
13. HackUPC - May 2-4, Barcelona, Catalunya, Barcelona, ES
14. HackDartmouth X - April 26-27, Hanover, New Hampshire, US
15. DragonHacks 11 - April 26-27, Philadelphia, PA, US
16. JacHacks - April 26-27, Quebec, Sainte-Anne-de-Bellevue, CA
17. MorganHacks - April 26-27, Baltimore, Maryland, US
18. Hacktech by Caltech - April 25-27, Pasadena, CA, US
19. LA Hacks - April 25-27, Los Angeles, California, US
20. HackDavis 2025 - April 19-20, Davis, California, US
21. UTA Datathon - April 12-13, Arlington, Texas, US
22. Hackabull - April 12-13, Tampa, Florida, US
23. Bit Hacks - April 11-13, Irvine, California, US
24. Bitcamp 2025 - April 11-13, College Park, Maryland, US

Please note that the dates and locations may be subject to change, and it's always a good idea to check the official website or contact the organizers for the most up-to-date information.

---

Question: What are some free hackathons?
Answer: Some of the free hackathons include:
1. GDG Solution Hacks 
2. SpurHacks 
3. Hack4Bengal 4.0 
4. Hack 4 Her 
5. Global Hack Week: GenAI 
6. MasseyHacks 
7. JAMHacks 9 
8. NMIT HACKS 2025 
9. DesignVerse at UCR 
10. HACKMESA 
11. Global Hack Week: Open Source Week 
12. GDSCHACKS 
13. HackUPC 
14. HackDartmouth X 
15. DragonHacks 11 
16. JacHacks 
17. MorganHacks 
18. Hacktech by Caltech 
19. LA Hacks 
20. HackDavis 2025 
21. UTA Datathon 
22. Hackabull 
23. Bit Hacks 
24. Bitcamp 2025 

Please note that this list may not be exhaustive as it is based on the provided data. For a complete and up-to-date list, you may want to check the relevant websites or sources.

---
**Milestone 5 — Generation and interface:**
