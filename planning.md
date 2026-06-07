# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

"hackthons or tech related events students can attend"
---

## Documents

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
| 9 | Devpost/Hackathons| web application with hackathons
| 10 | MLH.io | place filled with hackathons| |

---

## Chunking Strategy

**Chunk size:** 300


**Overlap:** 60

**Reasoning:** simple text on the information on the hackathon. Fits best for quick responses in a structured manner.

---

## Retrieval Approach


**Embedding model:** "llama-3.3-70b-versatile"

**Top-k:** 300

**Production tradeoff reflection:** Some responses are intentionally concise because the bot prioritizes information from its hackathon focused training data. Given the scope of this project, I focused on core functionality and retrieval quality. For a production or public facing deployment, I would invest additional effort in response refinement, broader knowledge coverage, and user experience improvements.

---

## Evaluation Plan



| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | "What are some upcoming hackathons?" |  "list of hackathons" |
| 2 | "What are some free hackathons?" | "list of free hackthons" |

| 3 | "Can you the winners from <hackathon name>?" | "Name or Names of previous winners" |
| 4 | "I want to focus on <field>, which tech event is best to gain the knowledge?"| "List of events that related to that spific field" |
| 5 | "What hackathons will be taking place near <address>? | "List of hackathons" |

---

## Anticipated Challenges

1. Events that arent related to my topic or common information not being listed

2. Not enough information on the provided response, E.Q the date it's taking place.

---

## Architecture

libaries being used include:

     - those seen in Rulebot, 
     - Ollama, 
     - requests

1. set up 'AI' with groq (or ollama)

2. Train on data inside class 'Sources', data from Reddit, MLH, and devpost

3. Embedding process with class 'Embedding' with provides vector storing, pretty much just breaking down the data and letting the AI create chunks

4. send data to frontend/gui with class 'GUI'  

---

## AI Tool Plan

     - AI being used are Claude, Ollama, Groq
     - give it inputs of quetions like those seen on planning.md 
     - What you expect it to produce
     - Verify the output matches my spec by making sure the data stays inside the trained data

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
